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
    def validate_message(self, message: Message)-> bool:
        """Run schema validation on a message received or sent."""
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
        """Validate that message matches an XSD schema."""
        from io import BytesIO
        from lxml import etree

        SCHEMAS = {
            'pacs.008.001.02': "impsepa/xsd/sepa-sct-2019/EPC115-06_2019_V1.0_pacs.008.001.02.xsd",
        }

        # Load the schema
        xsdfile = SCHEMAS[message.msgtype]  # FIXME: no error handling
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
