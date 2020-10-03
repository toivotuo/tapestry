from django.contrib import admin

from .models import SepaRoute

@admin.register(SepaRoute)
class SepaRouteAdmin(admin.ModelAdmin):
    list_display = (
        'external_key',
        'bic',
        'reachable_via',
        'reachability_type',
        'intermediary_bic',
    )

    list_filter = (
        'scheme',
        'reachable_via',
        'reachability_type',
    )
