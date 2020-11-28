SIC IMP
=======

The SIC IMP provides an Interface Message Processor (IMP)
implementation for the credit transfer schemes of Swiss Interbank
Clearing (SIC) in CHF. Support is also provided for the EuroSIC
facility operated by the Swiss Euro Clearing Bank (SECB) for SEPA
compliant payments in EUR.

Only SIC and EuroSIC credit transfer support is envisioned. Direct
debits are thus excluded from the scope.

Payments in Switzerland
-----------------------

Switzerland presents a case of a jurisdiction and a payments market
that is partially integrated with the payments in the EU/EEA. While
Switzerland is not an EU or EEA member, it is bound to the EU single
market via a web of bilateral agreements. As a non-EEA member,
Switzerland does not adopt EU legislation and has not developed a
legislative framework for payment services that would be harmonised
with the EU framework.

By virtue of geography and trade relations, however, the euro is
widely used in Swiss international trade along with the domestic
currency, the Swiss franc (CHF). Switzerland is also a participant of
the Single Euro Payment Area (SEPA) payment schemes.

For payments in CHF, a single hybrid RTGS-DTNS system, the SIC (Swiss
Interbank Clearing), is operated by a private sector entity, the SIX
Group (SIX), on behalf of the Swiss National Bank (SNB), the central
bank. Liechtenstein, an EEA member, shares the CHF as a national
currency with Switzerland and participates in the SIC and EuroSIC
systems.

For payments in EUR, Switzerland is a participant in SEPA for the
European Payments Council (EPC) payment schemes and payment
instruments. PSPs domiciled in Switzerland are eligible to participate
in the SEPA schemes and process EUR payments. To streamline access to
the SEPA infrastructures, the SECB operates the EuroSIC payment system
for SEPA Credit Transfer (SCT) payments.

The SIC system has completed migration to ISO 20022 standards and
broadly uses the same payment messages as the SEPA Credit Transfer
(SCT) payment scheme from the EPC. The EuroSIC system uses the SEPA
payment schemes as is.

New versions of interbank implementation guidelines (IG) are released
for SIC annually in November. These Swiss Payment Standards, which are
supported by all Swiss financial institutions, are based upon the
basic documentation issued by the ISO and the EPC and are reflected in
the two rulebooks, the “Swiss Business Rules” and the “Swiss
Implementation Guidelines”.

Routing and reach information for SIC is provided by a "bank master"
database published b SIX. Different versions, including a JSON
download, are available for public access. Only one CSM is available
making routing decisions straightforward.

Connectivity is available via three channels: via a "messaging
gateway" with two alternative commercial operators, via SWIFT or via a
web portal. Multiple vendors offer messaging gateway compliant
software that a PSP can operate internally or via a service bureau.

Implementing SIC credit transfer support
----------------------------------------

Support for EuroSIC in Tapestry is available directly through the SEPA
IMP. For SIC support, some rudimentary implementation work has been
done. More complete SIC support would ideally be based on the SEPA IMP
or a shared ISO 20022 credit transfers base IMP. The data elements in
SIC and SEPA SCT are rather similar and would support code sharing.

A mapping between SIC and SEPA SCT ISO 20022 message types and
versions is included in the Tapestry code.

Implementing Swiss direct debit support
---------------------------------------

Currently, Tapestry does not have direct debit support. To add support
for Swiss direct debit payment schemes, the SEPA IMP would initially
need to be upgraded to support the SEPA Direct Debit (SDD) payment
schemes. Then, the Swiss LSV+ (akin to SDD Core) and BDD (akin to SDD
B2B) could be added based on the SEPA SDD implementation.
