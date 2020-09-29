import uuid
from django.db import models

class Message(models.Model):
    """ Represents a single model exchanged via the FEX. """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    msgtype = models.CharField(max_length=140, blank=False)
    # FIXME: Should store 'payload' in AWS S3 or similar.
    payload = models.TextField(blank=False)


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
