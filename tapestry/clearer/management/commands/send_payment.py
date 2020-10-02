# Debugging management command to send a single payment packet.

import time
import yaml
import pprint
from rsmq import RedisSMQ
from rsmq.cmd.exceptions import QueueAlreadyExists, NoMessageInQueue
from django.core.management.base import BaseCommand, CommandError

pp = pprint.PrettyPrinter()

class Command(BaseCommand):
    help = "Send a single payment to clearing"

    def add_arguments(self, parser):
        parser.add_argument('source', nargs=1, type=str)
        parser.add_argument('destination', nargs=1, type=str)
        parser.add_argument('payload_file', nargs=1, type=str)

    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def notice(self, message):
        self.stderr.write(self.style.NOTICE(message))

    def handle(self, *args, **options):

        # Setup the queue where the router is waiting

        qname = "{}_{}".format(options['source'][0], "recv")
        queue = RedisSMQ(host="127.0.0.1", qname=qname)

        # Read the payload from file

        with open(options['payload_file'][0]) as fh:
            payload = fh.read()

        # Send the payment packet

        message_id = queue.sendMessage().message(payload).execute()

        self.success("Payment payload delivered: {}".format(message_id))
