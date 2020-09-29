import time
import sys
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Put a single message to the exchanger"

    def add_arguments(self, parser):
        parser.add_argument(
            "msgtype", nargs=1, type=str,
            help="Type of the message")
        parser.add_argument(
            "filename", nargs=1, type=str,
            help="Name of a file with the message or '-' for stdin")

        # FIXME: We could just default to stdin if the filename is not given.

    def success(self, message):
        self.stderr.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        from fex.models import Message

        msgtype = options['msgtype'][0]
        filename = options['filename'][0]

        if filename == '-':
            fh = sys.stdin
        else:
            fh = open(filename)

        msg = Message.objects.create(
            msgtype=msgtype,
            payload=fh.read(),
        )

        fh.close(
)
        self.success("Message put success: {} {} {}".format(
            msg.pk, msg.uuid, msg.msgtype))
