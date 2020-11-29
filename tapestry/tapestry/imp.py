# Message processor base class.

import abc
from fex.models import Message


class MessageProcessorError(Exception):
    pass


class MessageProcessor(abc.ABC):
    """Abstract base class for Interface Message Processors (IMPs).

    Sub-classes should be implemented for each payment scheme to do
    the processing according to what a scheme needs.
    """
    # FIXME: Should the processor be initiated with the incoming
    # message instead of passing the messages to each method? That
    # would be a more logical paradigm.


    @abc.abstractproperty
    def scheme(self):
        """Return the processor's supported scheme."""
        pass

    @abc.abstractmethod
    def can_process(self, message: Message) -> bool:
        """Can this message processor handle the message scheme?"""
        pass

    @abc.abstractmethod
    def validate_message(self, message: Message) -> bool:
        """Run schema validation on a message received or sent."""
        pass

    @abc.abstractmethod
    def debulk_message(self, message: Message) -> list:
        """Split a message into single payments."""
        pass

    @abc.abstractmethod
    def create_payments(self, payments: list) -> list:
        """Create payments from a debulked message."""
        pass
