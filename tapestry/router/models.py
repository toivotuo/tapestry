import uuid
from django.db import models
from django.conf import settings
from localflavor.generic.models import BICField
from django_countries.fields import CountryField
from tapestry.constants import PaymentSchemeChoice
from impsepa.constants import SepaCsmChoice

class SepaRoute(models.Model):
    """Represent an available route to a SEPA destination."""

    # FIXME: Could terminology here be aligned with BGP4?

    # FIXME: We must store here the source of where the data comes
    # from. Which directory and which version of the directory.

    class ReachabilityChoice(models.TextChoices):
        DIRECT = 'direct', 'Direct Participant'
        INDIRECT = 'indirect', 'Indirect Participant'
        UNKNOWN = 'unknown', 'Unknown'

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    scheme = models.CharField(max_length=70, blank=False,
                              choices=PaymentSchemeChoice.choices)
    external_key = models.CharField(max_length=16, blank=True)
    bic = BICField(blank=False)
    psp_name = models.CharField(max_length=140, blank=False)
    psp_city = models.CharField(max_length=35, blank=True)
    psp_country = CountryField(blank=True)
    reachable_via = models.CharField(max_length=4, blank=True,
                                     choices=SepaCsmChoice.choices)
    reachability_type = models.CharField(max_length=16, blank=False,
                                          choices=ReachabilityChoice.choices)
    intermediary_bic = BICField(blank=True)
    preferred_route = models.BooleanField(default=False)
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'SEPA route'
