import django.dispatch

# FIXME: Problem with using signals instead of message queues is that
# we don't get the abstraction of a port or an interface implemented.

clearer_packet_ingress = django.dispatch.Signal(
    providing_args=['packet'])

clearer_packet_egress = django.dispatch.Signal(
    providing_args=['packet'])
