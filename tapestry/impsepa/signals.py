import logging

logger = logging.getLogger(__name__)

def fex_message_received(sender, **kwargs):
    from impsepa.processors import SCTSEPAProcessor
    from fex.models import Message

    msg = Message.objects.get(pk=kwargs['message'])
    logger.info("Processing fex.Message: %s %s %s",
                msg.pk, msg.scheme, msg.msgtype)

    sct = SCTSEPAProcessor()

    if not sct.can_process(msg):
        return  # nothing to do here

    res = sct.validate_message(msg)

    return res
