from django.db import models
from django.core import validators


# FIXME: Add UUID for all the models for reference in RESTful APIs.

class TransactionManager(models.Manager):

    def add_transaction(self, currency, transfers):
        """Add a single Transaction where 'currency' is the Transaction
        currency, and 'transfers' is a list of data to create Transfer
        objects with keys 'account', 'amount' and 'description'. The
        'account' is an Account.handle. The Account is created if it
        doesn't exist. The amounts of all Transfers must add up to a
        zero. Returns the created Transaction.

        """
        # FIXME: Run in a database transaction!

        from decimal import Decimal
        transfer_sum = Decimal()

        # Create the Transaction to hold the Transfers
        tx = Transaction.objects.create(
            currency=currency,
        )

        # Create the Transfers
        for t in transfers:
            account = Account.objects.get_or_create(
                handle=t['account'],
                currency=tx.currency,
            )[0]
            amount = Decimal(t['amount'])
            Transfer.objects.create(
                transaction=tx,
                account=account,
                amount=amount,
                description=t.get('description', ''),
            )
            transfer_sum += amount

        if transfer_sum:
            # FIXME: Is there a more Django native exception to raise?
            raise ValueError("Transfers of a Transaction must sum to zero")

        return tx

class Transaction(models.Model):
    """A Transaction represents a single accounting journal entry that
    groups together one or more debits and credits on Accounts as
    represented by Transfers.

    """
    # FIXME: We do not have validation on database level that the
    # Transfers of a Transaction sum to zero.

    currency = models.CharField(
        max_length=3,
        blank=False,
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(3),
        ]
    )
    description = models.CharField(max_length=140, blank=True)

    objects = TransactionManager()

    def __str__(self):
        return "{} {}".format(self.pk, self.currency)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(currency__regex=r'^[A-Z]{3}$'),
                                   name='transaction_currency_regex_alpha3'),
        ]

class Transfer(models.Model):
    """A Transfer is a single debit or a credit on an Account. Multiple
    Transfers are grouped together by a Transaction to form a single
    accounting journal entry. Positive amounts represent debits and
    negative amounts credits.

    """
    account = models.ForeignKey("ledger.Account", on_delete=models.PROTECT)
    transaction = models.ForeignKey("ledger.Transaction", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.CharField(max_length=140, blank=True)

class Account(models.Model):
    """An Account is an accounting account on which sums can be debited or
    credited by a Transfer. Each Account is addressable by a unique
    handle.

    """
    handle = models.CharField(max_length=35, unique=True)
    currency = models.CharField(
        max_length=3,
        blank=False,
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(3),
        ]
    )
    description = models.CharField(max_length=140, blank=True)

    def get_balance(self):
        from decimal import Decimal
        # FIXME: There must be a more elegant way to do this!
        return Account.objects.filter(pk=self.pk).aggregate(balance=models.Sum('transfer__amount'))['balance'] or Decimal()

    def __str__(self):
        return "{} {} {}".format(self.pk, self.handle, self.currency)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(currency__regex=r'^[A-Z]{3}$'),
                                   name='accoount_currency_regex_alpha3'),
        ]
