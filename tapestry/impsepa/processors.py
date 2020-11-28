# Processors for the SEPA.

from fex.models import Message
from tapestry.imp import MessageProcessor
from tapestry.imp import MessageProcessorError


class SEPAProcessor(MessageProcessor):
    pass


class SCTSEPAProcessor(SEPAProcessor):
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
            raise MessageProcessorError("Message type not supported: {} {}".format(
                message.scheme, message.msgtype))
        with open(xsdfile) as xsdfd:
            xmlschema_doc = etree.parse(xsdfd)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # Validate the message against the schema
        doc = etree.parse(BytesIO(message.payload))
        try:
            xmlschema.assertValid(doc)
        except etree.DocumentInvalid as e:
            raise MessageProcessorError(str(e))

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

        # FIXME: It might make sense to convert this data dict (JSON)
        # with 'xmltodict' and use those path lookups instead of doing
        # this with XPath. It is easier to recreate the messages again
        # from dicts than construct XML with 'lxml' (but 'pyxb' could
        # help here). Using the WAPI+ standards [at least in the PSU
        # interface] would be even nicer.

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
