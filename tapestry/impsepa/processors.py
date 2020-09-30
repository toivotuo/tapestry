# Processors for the SEPA.

import abc

class ProcessorError(Exception):
    pass

class Processor(abc.ABC):  # FIXME: name better and move elsewhere
    """An abstract base class for Interface Message Procesors (IMPs) of
    different payment schemes that defines abstract methods.

    """
    @abc.abstractproperty
    def scheme(self):
        """ What scheme is this processor for? """
        pass

    @abc.abstractmethod
    def validate_message(self, message):
        """
        Runs schema validation on a message received or sent.
        """
        pass

class SEPASCTProcessor(Processor):
    @property
    def scheme(self):
        return "eu.sepa.sct"

    def validate_message(self, message):
        """ Validate that message matches the XSD schema. """
        from io import StringIO, BytesIO
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
