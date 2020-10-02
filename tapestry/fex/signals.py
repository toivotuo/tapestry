import django.dispatch

message_received = django.dispatch.Signal(
    providing_args=['message'])
