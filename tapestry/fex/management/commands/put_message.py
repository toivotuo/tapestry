"""Put a single message to the exchanger."""

import sys
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Put a single message to the exchanger"

    def add_arguments(self, parser):
        parser.add_argument(
            "scheme",
            nargs=1,
            type=str,
            help="Scheme of the message")
        parser.add_argument(
            "msgtype",
            nargs=1,
            type=str,
            help="Type of the message")
        parser.add_argument(
            "filename",
            nargs=1,
            type=str,
            help="Name of a file with the message or '-' for stdin")

        # FIXME: We could just default to stdin if the filename is not given.

    def success(self, message):
        self.stderr.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        from fex.models import Message
        from fex.signals import message_received

        scheme = options['scheme'][0]
        msgtype = options['msgtype'][0]
        filename = options['filename'][0]

        if filename == '-':
            fh = sys.stdin  # FIXME: Likely doesn't work as doesn't do binary
        else:
            fh = open(filename, 'rb')
        data = fh.read()
        fh.close()

        msg = Message.objects.create(
            scheme=scheme,
            msgtype=msgtype,
            payload=data,
        )

        # FIXME: This signal should really not be sent here! Also,
        # Message.__class__ doesn't seem to send really the class.
        responses = message_received.send(Message.__class__, message=msg.pk)

        # FIXME: Do actual validation of the responses and then save
        # that the message has been processed.

        self.success("Message put success: {} {} {} {}".format(
            msg.pk, msg.uuid, msg.scheme, msg.msgtype))
