# Debugging management command to add a single transaction to the
# accounting module of the Settler.

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Add a single transaction"

    def add_arguments(self, parser):
        parser.add_argument('currency', nargs=1, type=str)
        parser.add_argument('transfers', nargs='+', type=str)

    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):
        from settler.models import Transaction

        currency = options['currency'][0]

        transfers = []
        for t in options['transfers']:
            (account, amount) = t.split(':')
            transfers.append({
                'account': account,
                'amount': amount,
            })

        tx = Transaction.objects.add_transaction(currency, transfers)

        self.success("Added transaction: {}".format(tx))
