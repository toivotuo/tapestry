# Draft code for the SEPA IMP's ingress message processor.

import yaml
from djxml import xmlmodels
from rsmq import RedisSMQ
from rsmq.cmd.exceptions import QueueAlreadyExists, NoMessageInQueue
from django.core.management.base import BaseCommand, CommandError

class FIToFICustomerCreditTransferV02(xmlmodels.XmlModel):

    class Meta:
        namespaces = {"x": "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.02"}

    debtor_iban = xmlmodels.XPathTextField(
        "//x:DbtrAcct/x:Id/x:IBAN")

    creditor_iban = xmlmodels.XPathTextField(
        "//x:CdtrAcct/x:Id/x:IBAN")

    debtor_bic = xmlmodels.XPathTextField(
        "//x:DbtrAgt/x:FinInstnId/x:BIC")

    creditor_bic = xmlmodels.XPathTextField(
        "//x:CdtrAgt/x:FinInstnId/x:BIC")

    amount = xmlmodels.XPathTextField(
        "//x:IntrBkSttlmAmt")

    currency = xmlmodels.XPathTextField(
        "//x:IntrBkSttlmAmt/@Ccy")

pacs008 = FIToFICustomerCreditTransferV02

class Command(BaseCommand):
    help = "Process an incoming SEPA message"

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str)

    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):
        # FIXME: This only works when there's a single transaction
        # <CdtTrfTxInf> in the pacs.008.

        filename = options['filename'][0]
        xml = open(filename, 'r').read()

        root = pacs008.create_from_string(xml)

        payment = {
            'source_iban': root.debtor_iban,
            'destination_iban': root.creditor_iban,
            'source_bic': root.debtor_bic,
            'destination_bic': root.creditor_bic,
            'amount': root.amount,
            'currency': str(root.currency),  # FIXME: django-xml is buggy here
            'payload': xml,
        }

        # Setup the queue where the router is waiting

        qname = "{}_{}".format(root.creditor_bic, "recv")
        queue = RedisSMQ(host="127.0.0.1", qname=qname)

        message_id = queue.sendMessage().message(yaml.dump(payment)).execute()

        self.success("Payment payload delivered: {}".format(message_id))
