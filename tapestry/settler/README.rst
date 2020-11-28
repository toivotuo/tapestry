Settler
=======

The Settler component supports the Router component in effecting the
settlements for payments cleared in the Clearer component. Each
payment transaction is settled individually against settlement
accounts maintained in the Ledger component for PSPs and PSUs
connected to a Tapestry instance. As each payment transaction is
individually cleared and settled in real-time the paradigm for
settlements is RTGS.

When the Router has resolved the sending and receiving PSPs of a
payment transaction through a call to the Clearer, the Router must
effect the settlement of the payment transaction. This is done through
a call to the Settler. As parameters of the call the Settler receives,
at minimum, an amount and the settlement accounts to debit (sending
PSP's account) and credit (receiving PSP's account). The Settler in
turn leverages the Ledger component to record the settlement of the
payment transaction.

The API the Settler provides to the Router for is modelled after the
Y-Copy service of the SWIFT FIN network. A synchronous authorisation
request is sent from the Router to the Settler. If the sending PSP has
sufficient balance on their settlement account, the payment
transaction between the sending and receiving PSPs is recorded, and a
successful authorisation response is returned. If settlement account
balance of the sending PSP is insufficient, the settlement of the
payment transaction is declined.
