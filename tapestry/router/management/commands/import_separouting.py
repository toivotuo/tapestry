"""Import a SWIFTRef 'SEPAROUTING' V3 file to the Router."""

import logging
import datetime
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Import a 'SEPAROUTING' data file as XML"

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            nargs=1,
            type=str,
            help="Name of the 'SEPAROUTING' XML file to import")

    def handle(self, *args, **options):
        """Read the 'SEPAROUTING' XML file with PyXB bindings, mangle the data
        records a bit, and create a SepaRoute in the database for each
        routing entry from the XML.
        """
        from router.xsd import separouting_v3
        from router.forms import SepaRouteForm

        filename = options['filename'][0]
        with open(filename) as fd:
            root = separouting_v3.CreateFromDocument(fd.read())

        # FIXME: Do this in a database transaction to make the
        # importing of the whole file atomic.

        for entry in root.separouting_v3:
            # FIXME: As we only support new entries and not the delta
            # files with changes, there should be a check on whether
            # entry with the same record key exists and then data just
            # should be updated.
            if entry.modification_flag != 'A':
                logger.warning("Failed to import record %s with unknown modification flag: %s",
                               entry.record_key, entry.modification_flag)
                continue
            start_date = entry.start_date
            if start_date:
                start_date = datetime.date(int(start_date[0:4]),
                                           int(start_date[4:6]),
                                           int(start_date[6:8]))
            reachability_type = entry.reachability
            if reachability_type is None:
                reachability_type = 'unknown'
            elif reachability_type == 'D':
                reachability_type = 'direct'
            elif reachability_type == 'I':
                reachability_type = 'indirect'
            scheme_types = {
                'SCT': 'eu.sepa.sct',
                'SDD CORE': 'eu.sepa.sddcore',
                'SDD B2B': 'eu.sepa.sddb2b',
            }
            data = {
                'scheme': scheme_types[entry.scheme],
                'external_key': entry.record_key,
                'bic': entry.bic,
                'psp_name': entry.institution_name,
                'psp_city': entry.city,
                'psp_country': entry.iso_country_code,
                'reachable_via': entry.payment_channel_id,
                'reachability_type': reachability_type,
                'intermediary_bic': entry.intermediary_institution_bic or '',
                'preferred_route': entry.preferred_channel_flag == 'P' and True or False,
                'valid_from': start_date,
                'valid_to': None,
            }
            form = SepaRouteForm(data=data)
            if not form.is_valid():
                logger.warning("Failed to add SEPA route '%s': %s",
                               entry.record_key, ', '.join(form.errors.keys()))
                continue
            route = form.save()

            logger.info("Added SEPA route '%s': %s %s %s",
                        route.external_key, route.bic, route.reachable_via, route.scheme)

        message = "Successfully imported file {}".format(filename)
        self.stderr.write(self.style.SUCCESS(message))
