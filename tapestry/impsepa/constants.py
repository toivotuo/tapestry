from django.db import models

class SepaCsmChoice(models.TextChoices):
    """
    Providers identifiers for the different SEPA scheme compatible
    CSMs. Naming follows the model in the SWIFTRef 'SEPAROUTING' file
    format.
    """
    # These are extracted from the SEPAROUTING sample files. The
    # schmeas do not have an enumeration for thse. The human readable
    # names are not from SWIFTRef data; they may or may not be
    # correct.
    EBAS = 'EBAS', 'STEP2 PE-ACH (Belgium)'
    STPA = 'STPA', 'FIXME STPA'
    CECB = 'CECB', 'CEC (Belgium)'
    DBSC = 'DBSC', 'SEPA-Clearer (Germany)'
    PBSD = 'PBSD', 'Sumclearing (Denmark)'
    IBPA = 'IBPA', 'Iberpay (Spain)'
    STET = 'STET', 'STET (France)'
    SCTI = 'SCTI', 'ICBPI/BI-COMP (Italy)'
    EQNS = 'EQNS', 'Equens (Netherlands)'
    KIRP = 'KIRP', 'Euro Elixir (Poland)'
    # The following are improvised. It is unknown what the real
    # ones are. The SWIFTRef schema specifications that are publicly
    # available do not have an enumeration for the different CSMs.
    CTRL = 'CTRL', 'CENTROlink (Lithuania)'
    TIPS = 'TIPS', 'TIPS (Germany)'
    CSIA = 'CSIA', 'CS.I (Austria)'
    DIAS = 'DIAS', 'DIAS (Greece)'
    BSRA = 'BSRA', 'BISERA7-EUR (Bulgaria)'
