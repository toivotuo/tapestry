File Exchanger
==============

.. The File Exchanger or 'fex' app provides facilities for a Tapestry
.. instance to send and receive payment messages from PSUs or PSPs as
.. well as from peer or upstream CSMs.

The FEX component provides “file exchanger” services and connects a
PSP or CSM running Tapestry to other PSPs and PSUs acting as customers
as well as to service provider PSPs. The FEX sends and receives single
payment messages or files containing batches of payment
messages. Separate sub-components of the FEX provide transport
services over different protocols used for payment message
exchange. The FEX provides L2 services of the payments protocol stack
(see Table [tbl:payment-system-layers-vs-data-networking]) and
leverages other L1 networks as an overlay.

.. Each payment message is represented by a 'Message' model.

.. FIXME, this text is copied from LyX and is not edited
