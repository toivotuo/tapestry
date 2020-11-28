"""
Services that are independent of the Settler's models can be defined here.
"""

class AuthorisationService(object):
    """Provides authorisation services and settlement services. Used in
    payment clearing by the Clearer application. Design influenced by
    the Y-COPY service of the SWIFTNet FINCopy Service. Synchronous
    incoming calls are akin to FIN MT096 messages ("Copy to Central
    Institution Message") and responses MT097 ("Copy Message
    Authorization/Refusal Notification")."""

    def authorise(self, payment):
        """Takes in a 'payment packet' akin to an MT103 ("Single Customer
        Credit Transfer")."""
        from decimal import Decimal
        from ledger.models import Transaction

        # FIXME: We're just accounting, but we're not checking
        # balances at all.

        Transaction.objects.add_transaction(
            currency=payment['currency'],
            transfers=[
                {
                    'account': payment['source_bic'],
                    'amount': Decimal(payment['amount']) * -1,
                },
                {
                    'account': payment['destination_bic'],
                    'amount': Decimal(payment['amount']) * +1,
                },
            ],
        )

        # FIXME: We just return an ack for everything.
        return True
