Router
======

.. FIXME, this text is copied from LyX and is not edited

The Router component sends and receives payment messages with a
generic routing header from the IMP components. The responsibility of
the Router is to use the data from the routing header to make
decisions on where to route each payment message. The Router is aware
of reachability of other PSPs through the ingestion of reach and
routing tables provided by other PSPs or CSMs that a PSP running
Tapestry is connected to (see Section
[sec:routing-payment-systems]). As part of the routing process the
Router makes calls to the Clearer and Settler components in order to
execute the clearing and settling actions of payment transaction
processing (see Figure [fig:clearing-steps] and Sections
[subsec:clearing-payment-transactions] and
[subsec:net-gross-settlement]). After a payment is successfully
routed, the Router sends returns it to the relevant IMP for delivery
to a PSP or PSU through the IMP and the FEX components.
