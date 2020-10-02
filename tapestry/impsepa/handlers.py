import logging
import yaml

logger = logging.getLogger(__name__)

# FIXME: Kind of sucky design that the bulk of the operative code for
# the SEPA IMP is now here in a signal handler. Not neat.

def fex_message_received(sender, **kwargs):
    from impsepa.processors import SCTSEPAProcessor
    from fex.models import Message

    msg = Message.objects.get(pk=kwargs['message'])
    logger.info("Processing fex.Message: %s %s %s",
                msg.pk, msg.scheme, msg.msgtype)

    sct = SCTSEPAProcessor()

    if not sct.can_process(msg):
        # Make sure this is a message for us.
        return  # nothing to do here

    # Do the logic of a SEPA message processing. Validate the message,
    # debulk the message and convert individual payments into
    # packets. Then hand each of these over to the router by firing a
    # signal.

    res = sct.validate_message(msg)
    payments = sct.debulk_message(msg)
    packets = sct.create_payments(payments)

    # FIXME: We probably should use JSON instead of YAML for the
    # payment packets and have nice schema validation.

    for packet in packets:
        packet = yaml.dump(packet)
        print(packet)

    return res
