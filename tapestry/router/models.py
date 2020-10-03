import uuid
from django.db import models
from django.conf import settings
from localflavor.generic.models import BICField
from django_countries.fields import CountryField


class SepaRoute(models.Model):
    """Represent an available route to a SEPA destination."""

    # FIXME: Could terminology here be aligned with BGP4?

    class ReachabilityChoice(models.TextChoices):
        DIRECT = 'direct', 'Direct Participant'
        INDIRECT = 'indirect', 'Indirect Participant'
        UNKNOWN = 'unknown', 'Unknown'


    SCHEME_CHOICES = [(s, s) for s in settings.SUPPORTED_PAYMENT_SCHEMES]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    scheme = models.CharField(max_length=70, blank=False, choices=SCHEME_CHOICES)
    external_key = models.CharField(max_length=16, blank=False)
    bic = BICField(blank=False)
    psp_name = models.CharField(max_length=140, blank=False)
    psp_city = models.CharField(max_length=35, blank=False)
    psp_country = CountryField()
    reachable_via = models.CharField(max_length=4, blank=True)
    reachability_type = models.CharField(max_length=16, blank=False,
                                          choices=ReachabilityChoice.choices)
    intermediary_bic = BICField(blank=True)
    preferred_route = models.BooleanField(default=False)
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)
