from django.forms import ModelForm
from .models import SepaRoute

class SepaRouteForm(ModelForm):
    class Meta:
        model = SepaRoute
        fields = (
            'scheme',
            'external_key',
            'bic',
            'psp_name',
            'psp_city',
            'psp_country',
            'reachable_via',
            'reachability_type',
            'intermediary_bic',
            'preferred_route',
            'valid_from',
            'valid_to',
        )
