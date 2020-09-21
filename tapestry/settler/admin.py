from django.contrib import admin
from django.utils.html import format_html

from settler.models import Transaction
from settler.models import Account

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'currency',
        'description',
    )

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    def balance(self):
        return "{:8.2f}".format(self.get_balance())

    list_display = (
        'pk',
        'handle',
        'currency',
        balance,
    )

    list_filter = (
        'currency',
    )
