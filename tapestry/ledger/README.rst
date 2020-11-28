Ledger
======

The Ledger component provides the facilities for a standard
double-entry accounting (bookkeeping) system. As payment systems are
ultimately accounting systems that maintain the obligations between
PSUs, PSPs and CSMs, the Ledger component is a crucial supporting
facility for clearing and settlement.

The Ledger can be used to maintain the settlement accounts for PSPs
and payment accounts for PSUs connected to a Tapestry instance. The
Ledger is connected to other components of Tapestry. For example, the
Settler component posts accounting entries to the Ledger for payment
transactions settled. Only once the payment transaction is posted in
the Ledger is it considered settled in Tapestry in its role as a CSM.

The Ledger can also be used by the Settler component to maintain
reservations on settlement accounts for PSPs and payment accounts for
PSUs. The Ledger thus maintains for each account a settled (posted)
balance as well as a reserved balance. Account reservations instructed
by the Clearer component are also maintained in the Ledger component.

Models in the Ledger
--------------------

The Ledger component includes the minimum set of database models
required to implement double-entry accounting. The "bookkeeping"
models are described below.

Account
    The Account model represents a single account in bookkeeping. An
    Account can represent settlement account for a PSP or a payment
    account for a PSU, or any financial accounts that an entity
    operating Tapestry requires. At minimum an Account has some
    identifying and type information as well as the currency in which
    the account is denominated, but mostly it serves as an object
    containing methods for balance inquiries and balance
    reservations.

Transaction
    The Transaction model represents a posting in an bookkeeping
    journal. At minimum, a Transaction has timestamp information and
    metadata for describing the bookkeeping entry.

Transfer
    The Transfer model represents a single debit or credit on an
    Account. Taken collectively, all Transfers and Accounts make up
    the general ledger (GL) of a bookkeeping system. At minimum, a
    Transfer contains the debit or credit amount as a signed integer
    or a decimal type. Whether an amount is a debit or a credit is
    indicated by the the sign: positive amounts are debits and
    negative amounts are credits. A Transfer has two foreign keys, one
    to the Account on which the debit or credit is posted and another
    to a Transfer that groups two or more Transfers together into a
    single journal entry.

An important invariant for the consistency of bookkeeping is that the
debits and credits must always balance, in effect, the sum of debit
and credit amounts must be zero. This invariant is implemented at the
Transaction model level where the foreign keys pointing from two or
more Transfer models to each Transaction must have a zero sum for all
the Transfer amounts.
