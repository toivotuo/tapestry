8583 IMP
========

The 8583 IMP is a planned implementation of an Interface Message
Processor (IMP) to support authorisation, clearing and settlement of
card payments. Compared to the other two IMPs (SEPA and SIC), the 8583
IMP must support pull, not push, payment instruments.

In a card payment transaction, the first step is an authorisation from
the payee PSU to the payer's PSP. The authorisation must be routed in
real-time through the FEX to the 8583 IMP and over to the Router. If
Tapestry is run as the payer's PSP, then the Router must call the
Ledger to make an authorisation on the payer's payment account.

If Tapestry is run as the PSP for the payee PSU, then the Router must
forward the authorisation request over to the payment infrastructure
of the relevant payment scheme such as Visa or Mastercard. The
authorisation request would thus pass the FEX and the 8583 IMP twice
making this a performance critical activity.

Whether Tapestry could be adapted to support credit transfer payments
such as for the SEPA and SIC IMPs as well as card payments with the
8583 IMP is an open question and to be explored in further research
and development work.
