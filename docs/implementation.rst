Implementation
==============

As the implementation language for Tapestry, Python_ (version 3.7.X)
was selected. Python was selected in part due to the author's
familiarity with the language and due to Python being a widely adopted
and approachable language with extensive standard library and
third-party open source libraries. A 'requirements.txt' is provided in
the GitHub repository that documents the third-party libraries used.

.. _Python: https://www.python.org/

The Django_ (version 3.1.X) web development framework was selected to
provide the core structure for Tapestry. Django is a free and open
source framework that easy to understand yet provides an extensive set
of features as standard. Like Python, Django has a thriving ecosystem
of open source libraries that allow extending its functionalities.

.. _Django: https://www.djangoproject.com/

Both Python and Django support rapid experimentation and
prototyping. This can be considered as a core asset in light of the
nature of Tapestry as a payments router prototype.

As its nature is as a prototype, the implementation of Tapestry is not
complete for a running payments router that could be connected to
payment systems processing payment transactions with "real money".

Django features
---------------

While Tapestry is not a "web application" as such, the core features
of Django are applicable for Tapestry. The primary Django features
used in Tapestry are as follows:

Django models and ORM
    Django comes with a powerful object relational
    mapper (ORM). With the ORM, Django translates Python classes
    derived from a Django model base class and constructed with special
    formatting to SQL queries. The ORM can be connected to a number of
    database backends through which Django supports various relational
    database management systems (RDBMS). For example, for Tapestry
    testing, the easy to use SQLite RDBMS can be used. Any production
    implementation developed from the Tapestry prototype could use,
    for example, the powerful PostgreSQL RDBMS. The core objects of
    Tapestry, for example, a "payment account", are expressed as
    Django models and accessed through the Django ORM.

Django admin views
    Django provides a builtin feature for the easy construction of
    web-based administrative interfaces to applications. With the
    Django admin views an operations console can be rapidly
    constructed. An operations console is a requirement for production
    operations of a payments router. In a prototype like Tapestry, an
    operations console can be used to interactively explore the state
    of the payments router database to inspect the processing of
    payments messages.

Django signals
    Django provides an efficient signals framework implementing the
    publish-subscribe (pubsub) paradigm. Signals can be defined and
    then listeners subscribed to the signals. When signals are invoked
    (published) the signal payload is passed to all the
    listeners. Even in a monolithic Django application the signals
    framework allows the development of clean boundaries between
    modules. An event driven architecture can be implemented with some
    ease. In a more production ready implementation a Kafka event log
    or other pubsub facility could be used to provide more
    distribution and scalability than can be achieved with a
    monolithic Django application.

.. _`Django REST Framework`: https://www.django-rest-framework.org/

Django REST Framework
    A third-party library, the `Django REST Framework`_ (DRF) provides
    powerful facilities to construct APIs using the "representational
    state transfer" or REST paradigm. Using DRF, external interfaces
    to expose functionalities of Tapestry to PSU customers and to
    other PSPs.
