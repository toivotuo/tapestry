"""
A management command to run a routing daemon to do payments clearing.
"""

# FIXME: This on its way to being deprecated in favour of the simpler
# Django signals based implementation that is used in development. A
# more decoupled architecture can then be developed later.

import time
import yaml
import pprint
from django.core.management.base import BaseCommand, CommandError
from rsmq import RedisSMQ
from rsmq.cmd.exceptions import QueueAlreadyExists, NoMessageInQueue

pp = pprint.PrettyPrinter()

# FIXME: Make the "payment packet" into a class that resembles an
# MT103 or a pacs.008. [Or make it at least a class, no matter what it
# resembles, probably not a pacs.008 as we want it to have a scheme
# agnostic header and otherwise simply transport the payload.]

class Command(BaseCommand):
    from clearer.services import RoutingService

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
                # Receive a payment packet
                try:
                    queue = queues['recv']
                    msg = queue.receiveMessage().execute()
                    # Process payload from YAML
                    packet = yaml.safe_load(msg['message'])
                    self.success("Payment packet received: {}".format(
                        self.format_payment(packet)))
                    queue.deleteMessage(id=msg['id']).execute()
                except NoMessageInQueue:
                    self.notice("No payment packets for {} [{}]".format(
                        bic, time.asctime()))
                    continue

                # Authorise a payment packet; if not authorised just
                # drop the packet.

                # FIXME: The payment packet should be an object and we
                # should have methods for routing etc around that. [Or
                # maybe not as we have a routing service for the
                # routing. But the payment packet should certainly be
                # an object.]

                routserv = RoutingService()

                if not routserv.authorise(packet):
                    # FIXME: Non-authorised packets should be returned
                    # to sender. The router would need to have more in
                    # the payment packet to describe what a returned
                    # packet is. Therefore we will need to have
                    # unified packet types.

                    self.success("Payment packet authorisation failed: {}".format(
                        self.format_payment(packet)))

                    continue  # we just drop the non-authorised packet

                self.success("Payment packet authorisation succeeded: {}".format(
                    self.format_payment(packet)))

                # Route the packet by finding out what the destination
                # interface is.

                destination_bic = routserv.route(packet)

                if not destination_bic:
                    self.error("No destination for payment packet {}".format(
                               self.format_payment(packet)))
                    continue

                self.success("Routing payment packet to destination: {}".format(
                        self.format_payment(packet)))

                # Pass the message along to the destination BIC.

                qname = "{}_{}".format(destination_bic, "send")
                queue = RedisSMQ(host="127.0.0.1", qname=qname)

                message_id = queue.sendMessage().message(
                    yaml.safe_dump(packet)).execute()

                self.success("Payment packet sent: {}".format(
                    self.format_payment(packet)))

            time.sleep(1)  # just so we don't use _all_ CPU

    def format_payment(self, payment):
        """ Helper to show payment packet as something more readable. """
        # FIXME: Having the packet as an object and with a __repr__
        # would be helpful.
        return "{} -> {} {} {}".format(
            payment['source_bic'], payment['destination_bic'],
            payment['amount'], payment['currency'],
        )
