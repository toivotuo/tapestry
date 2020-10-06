from django.db import models

# FIXME: Would be important to have the regulatory descriptions
# everywhere and be able to generate Sphinx docs that can be used to
# present the APIs even where code doesn't exist.

class PaymentAccount(models.Model):
    currency = models.CharField(max_length=3)
    # FIXME: Use django-countries to validate the currency.

    def reserve_funds(self):
        """Make a reservation of value. Can be used for e.g. card payment
authorizations as well as for reserving funds before executing an
instant credit transfer like SCT Inst."""
        # FIXME: Needs a table to keep the reservations.
        raise NotImplementedError()

    def can_debit(self, amount):
        """Can an amount be debited (withdrawn from a PSUs perspective) from the
payment account?"""
        raise NotImplementedError()

    def can_credit(self, amount):
        """Can an amount be credited (deposited from a PSUs perspective) to the
payment account?"""
        raise NotImplementedError()

# We run the payment account now initially as single entry accounting
# system for efficiency. Every entry for the payment account is
# shadowed in double entry in the (future) GL module.

class PaymentAccountEntry(models.Model):
    payment_account = models.ForeignKey('host.PaymentAccount')
    amount = models.DecimalField()

    # FIXME: Isn't the efficiently GraphQL queryable payments
    # repository separate. Maybe the payment account should rather
    # have a sequence of events through which the double entry GL or
    # single entry payments repository are constructed?

    # FIXME: When funds are available on a payment account, an event
    # must be generated. Whether a push notification is then generated
    # or camt.XXX is then based on what listeners there are in a
    # pub-sub decoupled architecture. [This sounds like Kafka as a
    # facility on the edges whereas code is still RPC.]
