File Exchanger
==============

The FEX component provides “file exchanger” services and connects a
PSP or CSM running Tapestry to other PSUs or PSPs acting as customers
as well as to service provider PSPs and other peer CSMs.

The FEX sends and receives single payment messages or files containing
batches of payment messages. Separate transport sub-components of the
FEX provide transport services over different protocols used for
payment message exchange.

Each payment message in the FEX is represented by a Message
model. Each Message contains source and destination information that
instructs how a transport sub-component should receive or send payment
messages. Any payment message received from a PSU, PSP or CSM is
forwarded to the relevant Tapestry Interface Message Processor (IMP)
for processing. Similarly, a payment message received from an IMP, is
sent to a PSU, PSP or CSM.

A set of configuration files in the YAML format are used as to
describe the the PSUs, PSPs and CSMs that the FEX exchanges payment
messages as peers. Also the schedules for file exchange can be
configured.

The FEX is designed as extensible so that additional transport modules
can be added. An example of a transport module would be support for
EBICS_, the file exchange protocol commonly used in Germany, France
and Switzerland in PSU-PSP scenarios. EBICS is also used for PSP-PSP
and PSP-CSM file exchanges. Classic payment message exchange using
SFTP would be another example of an exchange protocol.

.. _EBICS: https://www.ebics.org/
