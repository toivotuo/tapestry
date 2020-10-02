from django.apps import AppConfig


class ClearerConfig(AppConfig):
    name = 'clearer'
    verbose_name = 'Clearer'

    def ready(self):
        from clearer.signals import clearer_packet_ingress
        from clearer.handlers import packet_received

        clearer_packet_ingress.connect(
            packet_received,
            dispatch_uid="clearer_packet_ingress_clearer",
        )
