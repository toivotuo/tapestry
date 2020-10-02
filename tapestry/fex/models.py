import uuid
from django.db import models
from django.conf import settings


class Message(models.Model):
    """Represent a single message exchanged via the FEX."""

    SCHEME_CHOICES = [(s, s) for s in settings.SUPPORTED_PAYMENT_SCHEMES]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    scheme = models.CharField(max_length=70, blank=False, choices=SCHEME_CHOICES)
    msgtype = models.CharField(max_length=140, blank=False)
    # FIXME: Should store 'payload' in AWS S3 or similar.
    payload = models.BinaryField(blank=False)

# FIXME: The ports of the counterparties with whom messages are
# exchanged are missing.

# FIXME: No timestamping here on receipt and processing of messages.

# FIXME: We need enums to validate the msgtype.

# FIXME: We need the concept of ports or interfaces that validates
# what the peer for message exchange is as well as what message types
# are accepted from the peer.

# FIXME: Configuration needed to decide which IMP to pass the file
# content.

# FIXME: Now that this is not a distributed application, each IMP
# class could provide a schema validator so that FEX could decline
# obviously invalid messages (not matching e.g. schema). Maybe for
# now, I'll just have a 'validated' boolean here. Using FSM instead of
# a bunch of booleans would be better though.
