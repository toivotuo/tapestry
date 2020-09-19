# Debugging management command to receive a single payment packet.

import time
import yaml
import pprint
from django.core.management.base import BaseCommand, CommandError
from rsmq import RedisSMQ
from rsmq.cmd.exceptions import QueueAlreadyExists, NoMessageInQueue

pp = pprint.PrettyPrinter()

class Command(BaseCommand):
    help = "Send a single payment for clearing"

    def add_arguments(self, parser):
        parser.add_argument('destination', nargs=1, type=str)

    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def notice(self, message):
        self.stderr.write(self.style.NOTICE(message))

    def handle(self, *args, **options):

        bic = options['destination'][0]

        # Setup the queue where the router delivering a packet from
        # waiting.

        qname = "{}_{}".format(bic, "send")
        queue = RedisSMQ(host="127.0.0.1", qname=qname)

        # Receive a payment packet
        try:
            msg = queue.receiveMessage().execute()
            # Process payload from YAML
            packet = yaml.safe_load(msg['message'])
            self.success("Payment packet received {}".format(
                self.format_payment(packet)))
            queue.deleteMessage(id=msg['id']).execute()
        except NoMessageInQueue:
            self.notice("No payment packets for {} ".format(
                bic))

    def format_payment(self, payment):
        """ Helper to show payment packet as something more readable. """
        # FIXME: Having the packet as an object and with a __repr__
        # would be helpful.
        return "{} -> {} {} {}".format(
            payment['source_bic'], payment['destination_bic'],
            payment['amount'], payment['currency'],
        )
