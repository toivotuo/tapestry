IMP
===

The IMP components provide “interface message processor” services for
different payment messaging standards. Each IMP component relies on
the FEX to send and receive payment messages or batches of payment
messages.

An IMP is responsible for bulking or debulking payment message batches
into individual payment messages. The individual payment messages are
then validated against the protocol supported by each IMP and the
rules of the payment scheme supported by the IMP. The IMPs implement
the input and output queues as well as protocol and payment scheme
validation.

An IMP is also responsible for extracting the relevant routing
information like IBAN and BIC or sort code from each single payment
message and wrapping the payment message with a generic routing
header. The Router component (through the Clearer and Settler
components) uses the routing header to implement clearing and
settlement as well as forwarding a payment message from a sending PSP
to a receiving PSP.

Each IMP provides a standard interface for interacting with a the FEX
for payment message interchange. Likewise, each IMP interacts with the
interface provided by the Router. The IMP interface is implemented as
a Python abstract base class, and IMPs for specific payment schemes
are implemented as sub-classes.
