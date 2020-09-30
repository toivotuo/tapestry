from django.apps import AppConfig


class ImpsepaConfig(AppConfig):
    name = 'impsepa'
    verbose_name = 'SEPA IMP'

    def ready(self):
        from fex.models import message_received
        from impsepa.signals import fex_message_received

        message_received.connect(
            fex_message_received,
            dispatch_uid="message_received_impsepa",
        )
