"""Import a SWIFTRef 'SEPAROUTING' V3 file to the Router."""

import sys
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

    def success(self, message):
        self.stderr.write(self.style.SUCCESS(message))

    def error(self, message):
        self.stderr.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        from router.models import SepaRoute
        from router.xsd import separouting_v3

        filename = options['filename'][0]
        with open(filename) as fd:
            root = separouting_v3.CreateFromDocument(fd.read())

        # FIXME: Use model form here to get extra validation,

        # FIXME: Do this in transaction to make the importing atomic.

        for entry in root.separouting_v3:
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
            route = SepaRoute.objects.create(
                scheme=entry.scheme,
                external_key=entry.record_key,
                bic=entry.bic,
                psp_name=entry.institution_name,
                psp_city=entry.city,
                psp_country=entry.iso_country_code,
                reachable_via=entry.payment_channel_id,
                reachablility_type=reachability_type,
                intermediary_bic=entry.intermediary_institution_bic or '',
                preferred_route=entry.preferred_channel_flag == 'P' and True or False,
                valid_from=start_date,
                valid_to=None,
            )

            logger.info("SEPA route added: %s %s %s", route.bic, route.reachable_via, route.scheme)

        message = "Successfully imported file {}".format(filename)
        self.stderr.write(self.style.SUCCESS(message))
