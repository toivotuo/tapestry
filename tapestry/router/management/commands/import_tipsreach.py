"""
Import the TARGET Instant Payment Settlement (TIPS) payment system
'participants and reachable parties' datafile as an Excel file. Note
that this is the informational reach table available from the ECB and
not the official TIPS Directory that would be used for production
routing.
"""
import logging
import datetime
import pandas as pd
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Import an TIPS reach table as Excel"

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            nargs=1,
            type=str,
            help="Name of the TIPS reach table file to import")

    def handle(self, *args, **options):
        """
        Read the TARGET Instant Payment Settlement (TIPS) payment system
        informative participants and reachable parties
        datafile. Useful for illustrating the reach of TIPS, but not
        for production payments routing purposes. For this the actual
        TIPS Directory available to participants from the ECB should
        be used.

        Todos:
            * Avoid creating duplicate entries on multiple runs
        """
        from router.forms import SepaRouteForm
        from tapestry.constants import PaymentSchemeChoice
        from impsepa.constants import SepaCsmChoice

        # Read the file to a pandas dataframe for processing.

        filename = options['filename'][0]
        df = pd.read_excel(filename, header=3)  # skip header fluff

        # Iterate over the rows of the dataframe.

        for index, row in df.iterrows():
            reachability_types = {
                'TIPS Participant': 'direct',
                'Reachable Party': 'indirect',
            }

            bic = row['USER BIC']
            psp_name = row['NAME OF THE FINANCIAL INSTITUTION']
            reachability_type = reachability_types[
                row['PARTICIPATION TYPE']
            ]

            data = {
                'scheme': PaymentSchemeChoice.EU_SEPA_SCTINST,
                'external_key': '',
                'bic': bic,
                'psp_name': psp_name,
                'psp_city': '',
                'psp_country': '',
                'reachable_via': SepaCsmChoice.TIPS,
                'reachability_type': reachability_type,
                'intermediary_bic': '',
                'preferred_route': None,
                'valid_from': None,
                'valid_to': None,
            }
            form = SepaRouteForm(data=data)
            if not form.is_valid():
                logger.warning("Failed to TIPS reachable route: %s",
                               ', '.join(form.errors.keys()))
                continue
            route = form.save()

            logger.info("Added TIPS reachable route: %s %s %s",
                        route.bic, route.reachable_via, route.scheme)

        message = "Successfully imported file {}".format(filename)
        self.stderr.write(self.style.SUCCESS(message))
