from django.contrib import admin
from django.utils.html import format_html

from settler.models import Transaction
from settler.models import Transfer
from settler.models import Account

class TransferInline(admin.TabularInline):
    model = Transfer

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'currency',
        'description',
    )

    inlines = (
        TransferInline,
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
