SEPA IMP
========

The SEPA IMP provides an Interface Message Processor (IMP)
implementation for the SEPA (Single Euro Payments Area) payment
schemes for EUR. Initially, only support for the SEPA Credit Transfer
(SCT) and SEPA Instant Credit Transfer (SCT Inst) payment schemes is
envisioned. The SEPA Direct Debit (SDD) payment schemes (Core and B2B)
are left for future consideration.

All SEPA payment schemes are defined and managed by the European
Payments Council (EPC). The payment schemes are based on ISO 20022
protocols and use XML for the encoding of payment messages. The
payment scheme standards from the EPC narrow the definitions is ISO
20022 to suit the use cases of the SEPA payment schemes. For example,
only EUR is supported as a currency.

Processing inbound SEPA SCT payment
-----------------------------------

Inbound payment messages in the SEPA SCT payment scheme are expressed
in the pacs.008 V2 (FIToFICustomerCreditTransfer) ISO 20022 format
as XML. Note that pacs.008 is used in PSP to PSP payment
transactions. For payment initiation messages from a PSU to a PSP, a
pain.001 payment message would be used.

The following is a rough outline of the steps in the processing of an
inbound pacs.008 payment message.

#. Validate the message against the relevant XML schema. Options
   include using the standard ISO 20022 XML Schema Description (XSD)
   file or the equivalent SCT XSD file from the EPC. If the ISO XSD is
   used, then the SCT validation for currencies and other limitations
   must be done separately.

#. Perform debulking of any payment message file. A pacs.008 may
   contain one or more payment messages. In the Tapestry
   implementation the Router, Clearer and Settler components only
   process a single message at a time in an RTGS-like clearing and
   settlement paradigm.

#. Add a routing header to the extracted payment message that contains
   a single payment transaction only. The routing header follows a
   standard payment scheme independent format that is proprietary to
   Tapestry, but allows the Router to perform payment scheme
   independent routing function.

#. Pass the raw payment message payload with the routing header to the
   Router component for clearing, settlement and further forwarding.
