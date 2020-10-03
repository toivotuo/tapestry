from django.db import models

class SepaCsmChoice(models.TextChoices):
    """
    Providers identifiers for the different SEPA scheme compatible
    CSMs. Naming follows the model in the SWIFTRef 'SEPAROUTING' file
    format.
    """
    EBAS = 'EBAS', 'STEP2 (Belgium)'
    STPA = 'STPA', 'FIXME STPA'
    CECB = 'CECB', 'CEC (Belgium)'
    DBSC = 'DBSC', 'SEPA-Clearer (Germany)'
    PBSD = 'PBSD', 'FIXME PBSD'
    IBPA = 'IBPA', 'Iberpay (Spain)'
    STET = 'STET', 'STET (France)'
    SCTI = 'SCTI', 'FIXME SCTI'
    EQNS = 'EQNS', 'Equens (The Netherlands)'
    KIRP = 'KIRP', 'Euro Elixir (Poland)'
    # FIXME: CTRL is improvised; unknown what the real code is.
    CTRL = 'CTRL', 'CENTROlink (Lithuania)'
