from django.db import models
from django.core import validators

# FIXME: Add UUID for all the models for reference in RESTful APIs.

class Transaction(models.Model):
    """A Transaction represents a single accounting journal entry that
    groups together one or more debits and credits on Accounts as
    represented by Transfers.

    """
    currency = models.CharField(max_length=3)
    description = models.CharField(max_length=140)

    objects = TransactionManager()

class Transfer(models.Model):
    """A Transfer is a single debit or a credit on an Account. Multiple
    Transfers are grouped together by a Transaction to form a single
    accounting journal entry. Positive amounts represent debits and
    negative amounts credits.

    """
    account = models.ForeignKey("settler.Account", on_delete=models.PROTECT)
    transaction = models.ForeignKey("settler.Transaction", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.CharField(max_length=140)

class Account(models.Model):
    """An Account is an accounting account on which sums can be debited or
    credited by a Transfer. Each Account is addressable by a unique
    handle.

    """
    handle = models.CharField(max_length=35, unique=True)
    currency = models.CharField(max_length=3)
    description = models.CharField(max_length=140)
