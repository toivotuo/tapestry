# A management command for the 'router' to do payments clearing.

import time
import yaml
import pprint
from django.core.management.base import BaseCommand, CommandError
from rsmq import RedisSMQ
from rsmq.cmd.exceptions import QueueAlreadyExists, NoMessageInQueue

pp = pprint.PrettyPrinter()

class Command(BaseCommand):
    help = "Runs the router for clearing payments"

    QUEUES = {}

    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def notice(self, message):
        self.stderr.write(self.style.NOTICE(message))


    def handle(self, *args, **options):

        # Load the configuration

        self.success("Booting the router by reading configuration...")

        # FIXME: Configuration needs to be better deployed (and not hardwired)
        with open("csm.yaml") as fh:
            config = yaml.load(fh.read(), Loader=yaml.FullLoader)

        bics = [x['bic'] for x in config['participants']]
        self.success("Found PSPs with BICs: {}".format(", ".join(bics)))

        # Setup queues for all the PSPs

        self.success("Setting up interface for each PSP...")

        for psp in config['participants']:
            bic = psp['bic']
            name = psp['name']
            for direction in ['send', 'recv']:
                qname = "{}_{}".format(bic, direction)
                queue = RedisSMQ(host="127.0.0.1", qname=qname)
                try:
                    queue.createQueue(delay=0, vt=20, quiet=True).execute()
                except QueueAlreadyExists:
                    pass
                self.QUEUES.setdefault(bic, {})
                self.QUEUES[bic][direction] = queue
            self.success("Interface set up for {} ({})".format(
                bic, name))

        # Start event loop trying to read messages from the different queues

        # FIXME: This is completely naive way to do this, but it is
        # intentional and will be switched over to Kafka at a later
        # stage.

        self.success("Listening for payment packets...")

        while True:
            for bic, queues in self.QUEUES.items():
                try:
                    queue = queues['recv']
                    msg = queue.receiveMessage().execute()
                    self.success("Message from {}: {}".format(bic, msg))
                    queue.deleteMessage(id=msg['id']).execute()
                except NoMessageInQueue:
                    self.notice("No payment packets for {} [{}]".format(
                        bic, time.asctime()))

            time.sleep(1)  # just so we don't use _all_ CPU
