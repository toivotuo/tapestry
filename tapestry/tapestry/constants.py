from django.db import models

class PaymentSchemeChoice(models.TextChoices):
    EU_SEPA_SCT = 'eu.sepa.sct', 'EU SEPA SCT'
    EU_SEPA_SCTINST = 'eu.sepa.sctinst', 'EU SEPA SCT Inst'
    EU_SEPA_SDDCORE = 'eu.sepa.sddcore', 'EU SEPA SDD CORE'
    EU_SEPA_SDDB2B = 'eu.sepa.sddb2b', 'EU SEPA SDD B2B'
    EU_SEPA_SCC = 'eu.sepa.scc', 'EU SEPA Card Clearing'
