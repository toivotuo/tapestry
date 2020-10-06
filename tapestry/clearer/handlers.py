import logging
import yaml

logger = logging.getLogger(__name__)

def packet_received(sender, **kwargs):
    from .services import RoutingService
    from .services import RoutingError

    logger.info("Clearer packet received: {}".format(sender))

    packet = yaml.safe_load(kwargs['packet'])

    routserv = RoutingService()

    # FIXME: Packets coming to be routed should have a UUID enabling
    # them to be tracked throughout the chain and also in log
    # messages.

    if not routserv.authorise(packet):
        # FIXME: Non-authorised packets are not handled; we simply
        # abort.
        logger.error("Failure to authorise a packet")
        raise RoutingError("Authorisation failed")

    logger.info("Payment packet authorisation succeeded: %s",
                routserv.format_payment(packet))

    # Route the packet by finding out what the destination
    # interface is.

    destination_bic = routserv.route(packet)

    if not destination_bic:
        logger.error("No destination for payment packet %s",
                     routserv.format_payment(packet))

    logger.info("Routing payment packet to destination: %s",
                routserv.format_payment(packet))
