Clearer
=======

The Clearer component supports the Router component in managing the
obligations of different PSPs and PSUs in the role of Tapestry as a
CSM. The Clearer provides real-time clearing against settlements
accounts maintained for PSPs and PSUs in the Ledger
component. Settlements are effected through the Settler component by the
Router.

The Clearer does not do netting and the clearing and settling paradigm
is closer to an RTGS than a DTNS. As the clearing and settling
paradigm is that of an RTGS, the Clearer does clearing on individual
payment transactions, one at a time. In a DTNS payment system, the
clearing step has some algorithmic complexity in calculating the
multilateral net positions between participating PSPs.

In an RTGS, it is sufficient only to ascertain that the sending PSP
has sufficient balance. As Tapestry implements an RTGS paradigm most
of the work of clearing and settlement is done by the Router and
Settler. The role of the Clearer is limited to looking up the sending
and receiving PSPs using the routing tables populated by the Router.
