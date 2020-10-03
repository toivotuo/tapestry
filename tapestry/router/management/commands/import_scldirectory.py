"""
Import a Deutsche Bundesbank SEPA-Clearer SCL-Directory file of
routing and reachability data.
"""
import logging
import datetime
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Import an SCL-Directory data file as XML"

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            nargs=1,
            type=str,
            help="Name of the SCL-Directory XML file to import")

    def handle(self, *args, **options):
        """
        Read the SCL-Directory XML file with PyXB bindings for the
        rocs.001.001.006 format, mangle the data records a bit, and
        create a SepaRoute in the database for each routing entry from
        the XML.

        Todo:
            * Add support for processing delta data files
            * Run in database transaction for atomicity
            * Support GrpHdr.FileValidityDate (now validity assumed)
        """
        from router.xsd import rocs_001_001_06
        from router.forms import SepaRouteForm

        filename = options['filename'][0]
        with open(filename) as fd:
            root = rocs_001_001_06.CreateFromDocument(fd.read()).rocs_001_001_06

        # Process the group header first...

        assert root.GrpHdr.PtyId.BICOrBEI == 'MARKDEFFXXX'
        assert root.GrpHdr.FullTable == 1

        # ...and now process the separate route entries.

        for entry in root.RchEntry:
            if entry.Status != 'existing':
                logger.warning("Failed to import entry with status flag: %s",
                               entry.status)
                continue

            # FIXME: R-transaction scheme types not supported
            scheme_types = {
                'SCT': 'eu.sepa.sct',
                'SDD core': 'eu.sepa.sddcore',
                'SDD b2b': 'eu.sepa.sddb2b',
                'SCC': 'eu.sepa.scc',
            }
            scheme_type = scheme_types[entry.Product.ProductName]

            if entry.Participant.NmAndAdr.Adr is not None:
                psp_country = entry.Participant.NmAndAdr.Adr.Strd.Ctry
            else:
                psp_country = ''

            if entry.CSM.PtyId.BICOrBEI == 'MARKDEFF':
                reachable_via = 'DBSC'
                reachability_type = 'direct'
            elif entry.CSM.PtyId.PrtryId.Id == 'Other CSM':
                reachable_via = 'DBSC'
                reachability_type = 'indirect'
            else:
                raise ValueError("Unknown CSM specification")

            data = {
                'scheme': scheme_type,
                'external_key': '',
                'bic': entry.Participant.BIC,
                'psp_name': entry.Participant.NmAndAdr.Nm,
                'psp_city': '',
                'psp_country': psp_country,
                'reachable_via': reachable_via,
                'reachability_type': reachability_type,
                'intermediary_bic': '',
                'preferred_route': entry.CSM.PreferredIndicator == 1 and True or False,
                # FIXME: valid_from and valid_to should be localised to German time
                'valid_from': entry.Validity.FrDtTm,
                'valid_to': entry.Validity.ToDtTm,
            }
            form = SepaRouteForm(data=data)
            if not form.is_valid():
                logger.warning("Failed to add SCL-Directory route: %s",
                               ', '.join(form.errors.keys()))
                continue
            route = form.save()

            logger.info("Added SCL-Directory route: %s %s %s",
                        route.bic, route.reachable_via, route.scheme)

        message = "Successfully imported file {}".format(filename)
        self.stderr.write(self.style.SUCCESS(message))
