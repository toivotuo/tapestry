# Debugging management command to dump the balance of all accounts in
# the accounting modules of the Settler.

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Dump the balance of all accounts"

    def add_arguments(self, parser):
        pass

    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):
        from decimal import Decimal
        from settler.models import Account

        accounts = Account.objects.filter().order_by('handle', 'pk')

        for account in accounts:
            print("{:>4} {:<16} {:>8.2f}".format(
                account.pk,
                account.handle or '-',
                account.get_balance(),
            ))
