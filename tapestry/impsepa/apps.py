from django.apps import AppConfig


class ImpsepaConfig(AppConfig):
    name = 'impsepa'
    verbose_name = 'SEPA IMP'

    def ready(self):
        from fex.signals import message_received
        from impsepa.handlers import fex_message_received

        message_received.connect(
            fex_message_received,
            dispatch_uid="message_received_impsepa",
        )
