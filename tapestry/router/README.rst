Router
======

The Router component sends and receives payment messages with a
generic routing header from the IMP components. It is the
responsibility of the Router to use the data from the routing header
to make decisions on where to route each payment message.

Reachability and routing
------------------------

The Router is aware of reachability to other PSPs through the
ingestion of reach and routing tables provided by other PSPs or CSMs
that a PSP running Tapestry is connected with. In the current
implementation of Tapestry a SepaRoute model is maintained in the
Router. Each SepaRoute instance describes a single route to a PSP
(represented by a BIC8 or a BIC11).

Routing tables can be ingested using Django management commands from
upstream CSMs as described below. Each routing table entry creates a
SepaRoute in Tapestry.

.. _PyXB: https://pabigot.github.io/pyxb/

import-separouting.py
    Ingests "SEPAROUTING" XML files provided as part of the SWIFT
    reference data "SEPA Plus" service. The file format lists
    reachable BICs and which SEPA payment schemes the BICs have
    adhered to, and through which CSMs the BIC can be reached. The
    Tapestry implementation uses the PyXB_ library to create Python
    bindings for an XSD.

import-scldirectory.py
    Ingests the SCL-Directory XML file with PyXB_ bindings for the
    rocs.001.001.006 reach table format. The SCL-Directory only
    contains PSPs reachable through the Deutsche Bundesbank operated
    SEPA-Clearer SEPA CSM. However, as the SEPA-Clearer peers with the
    STEP2 PE-CSM, the coverage of reachable PSPs in the SCL-Directory
    is comprehensive.

import-tipsreach.py
    Ingests the TARGET Instant Payment Settlement (TIPS) CSM
    informative participants and reachable parties data file for SEPA
    SCT Inst. Useful for illustrating the reach of TIPS, but not for
    production payments routing purposes. For this the actual TIPS
    Directory available to participants from the ECB should be
    used. The data file is delivered as an Excel file and a Python
    library is used to parse the file and extract routing
    entries.

In terms of the richness of routing data, SEPAROUTING and
SCL-Directory data files are comprehensive, but the TIPS data file only
describes BICs that are reachable via the TIPS CSM. It should also be
noted that SEPAROUTING and SCL-Directory data files cover SEPA SCT
while the TIPS data file covers SEPA SCT Inst.

Clearing and settlement
-----------------------

As part of the routing process the Router makes calls to the Clearer
and Settler components in order to execute the clearing and settling
actions of payment transaction processing.

After a payment is successfully routed, the Router sends returns it to
the relevant IMP for delivery to a PSP or PSU through the IMP and the
FEX components.
