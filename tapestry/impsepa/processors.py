# Processors for the SEPA.

import abc
from fex.models import Message


class ProcessorError(Exception):
    pass


# FIXME: Maybe these should be just called MessageProcessor?

class Processor(abc.ABC):  # FIXME: name better and move elsewhere
    """Abstract base class for Interface Message Processors (IMPs).

    Sub-classes should be implemented for each payment scheme to do
    the processing according to what a scheme needs.
    """
    # FIXME: Should the processor be initiated with the incoming
    # message instead of passing the messages to each method? That
    # would be a more logical paradigm.


    @abc.abstractproperty
    def scheme(self):
        """Return the processor's supported scheme."""
        pass

    @abc.abstractmethod
    def can_process(self, message: Message) -> bool:
        """Can this message processor handle the message scheme?"""
        pass

    @abc.abstractmethod
    def validate_message(self, message: Message) -> bool:
        """Run schema validation on a message received or sent."""
        pass

    @abc.abstractmethod
    def debulk_message(self, message: Message) -> list:
        """Split a message into single payments."""
        pass

    @abc.abstractmethod
    def create_payments(self, payments: list) -> list:
        """Create payments from a debulked message."""
        pass


class SEPAProcessor(Processor):
    pass


class SCTSEPAProcessor(SEPAProcessor):  # FIXME: unreadable class name
    @property
    def scheme(self):
        return "eu.sepa.sct"

    def can_process(self, message):
        if self.scheme == message.scheme:
            return True
        return False

    def validate_message(self, message):
        """Validate that message matches a SEPA XSD schema."""
        from io import BytesIO
        from lxml import etree

        assert message.scheme == 'eu.sepa.sct'

        # FIXME: We should be doing much more validation here beyond
        # just validating the schema.

        SCHEMAS = {
            'pacs.008.001.02': "impsepa/xsd/sepa-sct-2019/EPC115-06_2019_V1.0_pacs.008.001.02.xsd",
        }

        # Load the schema
        xsdfile = SCHEMAS.get(message.msgtype, None)
        if xsdfile is None:
            raise ProcessorError("Message type not supported: {} {}".format(
                message.scheme, message.msgtype))
        with open(xsdfile) as xsdfd:
            xmlschema_doc = etree.parse(xsdfd)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # Validate the message against the schema
        doc = etree.parse(BytesIO(message.payload))
        try:
            xmlschema.assertValid(doc)
        except etree.DocumentInvalid as e:
            raise ProcessorError(str(e))

        return True  # valid message

    def debulk_message(self, message):
        """Split a SEPA payment message into individual payments."""
        from io import BytesIO
        from lxml import etree

        assert message.scheme == 'eu.sepa.sct'
        assert message.msgtype ==  'pacs.008.001.02'  # only type supported

        # FIXME: Architecture here is not efficient as we process the
        # message with lxml multiple times. Better to put the message
        # to the class instance and process it only once. Will need a
        # bit of refactoring to get there.

        doc = etree.parse(BytesIO(message.payload))

        namespaces = {
            'pacs': 'urn:iso:std:iso:20022:tech:xsd:pacs.008.001.02'
        }

        payments = doc.xpath('//pacs:Document/pacs:FIToFICstmrCdtTrf/pacs:CdtTrfTxInf',
                             namespaces=namespaces)

        return payments

    def create_payments(self, payments):
        """Create payment packets ready for the Clearer."""
        from lxml import etree

        namespaces = {
            'pacs': 'urn:iso:std:iso:20022:tech:xsd:pacs.008.001.02'
        }

        packets = []

        for payment in payments:
            debtor_iban = payment.xpath(
                "//pacs:CdtTrfTxInf/pacs:DbtrAcct/pacs:Id/pacs:IBAN",
                namespaces=namespaces)

            creditor_iban = payment.xpath(
                "//pacs:CdtTrfTxInf/pacs:CdtrAcct/pacs:Id/pacs:IBAN",
                namespaces=namespaces)

            debtor_bic = payment.xpath(
                "//pacs:CdtTrfTxInf/pacs:DbtrAgt/pacs:FinInstnId/pacs:BIC",
                namespaces=namespaces)

            creditor_bic = payment.xpath(
                "//pacs:CdtTrfTxInf/pacs:CdtrAgt/pacs:FinInstnId/pacs:BIC",
                namespaces=namespaces)

            amount = payment.xpath(
                "//pacs:CdtTrfTxInf/pacs:IntrBkSttlmAmt",
                namespaces=namespaces)

            currency = payment.xpath(
                "//pacs:CdtTrfTxInf/pacs:IntrBkSttlmAmt/@Ccy",
                namespaces=namespaces)

            packet = {
                'source_iban': debtor_iban[0].text,
                'destination_iban': creditor_iban[0].text,
                'source_bic': debtor_bic[0].text,
                'destination_bic': creditor_bic[0].text,
                'amount': amount[0].text,
                'currency': str(currency[0]),
                'payload': etree.tostring(payment),
            }

            packets.append(packet)

        return packets
