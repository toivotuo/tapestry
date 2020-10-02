import logging
import yaml

logger = logging.getLogger(__name__)

def packet_received(sender, **kwargs):
    logger.info("Clearer packet received: {}".format(sender))
