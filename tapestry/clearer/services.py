"""Implementation of a payments router. Takes payment packets as input
on ingress ports (interfaces), makes routing decisions and sents
packets out on egress ports."""

class RoutingError(Exception):
    pass


class RoutingService(object):
    """Provides a payments routing facility. Takes in a payment packet and make a routing (forwarding) decision on where to send the packet."""

    def authorise(self, payment):
        """Authorise a single payment packet via the settlement module."""
        from settler.services import AuthorisationService
        authserv = AuthorisationService()
        return authserv.authorise(payment)

    def route(self, payment):
        """Route a single packet by finding its destination interface (BIC)."""
        # FIXME: No routing logic happening here except we simply use
        # the destination BIC.
        return payment['destination_bic']

    def format_payment(self, payment):
        """Helper to show payment packet as something more readable."""
        # FIXME: Having the packet as an object and with a __repr__
        # would be helpful.
        return "{} -> {} {} {}".format(
            payment['source_bic'], payment['destination_bic'],
            payment['amount'], payment['currency'],
        )
