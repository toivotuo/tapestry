"""Get a single message from the exchanger."""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Get a single message from the exchanger"

    def add_arguments(self, parser):
        parser.add_argument("msgid",
                            nargs=1,
                            type=str,
                            help="Identifier of the message")

    def success(self, message):
        self.stderr.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        from fex.models import Message

        msgid = options['msgid'][0]

        msg = Message.objects.get(pk=msgid)

        self.success("Message get success: {} {} {}".format(
            msg.pk, msg.uuid, msg.msgtype))

        print(msg.payload)
