Introduction
============

Background and objectives
-------------------------

Tapestry is a set of experiments in developing a multi-scheme
"clearing and settlement mechanism" (CSM) for account to account
payments between "payment service providers" (PSP) such as banks and
other financial institutions. Tapestry is not production quality
software. It is best understood in the tradition of operating systems
developed to teach computer science concepts. Minix and Xv6 are
examples of Unix-like teaching operating systems.

With Tapestry the teaching objective is "payments engineering" and the
target audience is software engineers who have at least some practice
in software development, but little or no exposure to financial
technology in general and payment systems in particular. The Tapestry
source code is designed to illustrate concepts in payment systems
through running code. By exploring and modifying the Tapestry source
code, a software engineer can develop a more intuitive understanding
and mental models of how payments work. developing this type of
understanding with production systems is more difficult due to system
complexity and often high degree of legacy code. Furthermore, access
to production payment systems is naturally rather limited unless one
is employed at a financial institution.

Tapestry has been developed as part of a Master's Thesis project in
Computer Science at the University of Helsinki. It is the idea that
the Tapestry code is explored with the thesis document as a
companion. Payment systems and related concepts are covered at some
length in the thesis.

Payments engineering
--------------------

Payments engineering has traditionally been, and to a degree still is,
an opaque area of software engineering. Payment systems - both as
utilities for bank to bank interactions - and within individual banks
have been developed as proprietary systems with little public
documentation available. Access to participate in payment systems as a
payment service provider has also been limited to only authorised
credit institutions (banks) and thus the barries for access have been
high. Starting in the 2000s and accelerating in the 2010s there has -
especially in Europe - been a concentrated effort to open access to
payment systems to new players such as e-money institutions, payment
institutions and third-party providers. At the same time a new crop of
service providers and financial institutions has entered the market
with solutions and services that leverage new technologies like
pervasive communications and mobile devices. With this rise of
"financial technology" or "fintech", an increasing number of software
developers are working on the engineering of payment
systems. Arguably, the supply of information on best practices for
payments engineering has not kept up with the demand from developers
new to the field.

On a high level, payments engineering is the development of software
systems for high volume transactional systems with strict criteria for
availability, accuracy, timeliness and overall robustness. The usual
paradigm in payment systems is that of message exchange. A payment
message is constructed by the sending PSP the represent the value that
a sending customer (a payment service user or PSU) wants to have
delivered to a receiving PSU that is a customer of the receiving
PSP. Between the sending and receiving PSP, a payment system
consisting of a set of rules (payment scheme) and technical components
(payment infrastructure) is responsible for delivery of the message as
well as with the transfer of value between the PSPs.

In engineering terms, a payment system can be compared to a
telecommunications network. Both provide a highly performant and
reliable exchange of messages. However, in the case of the payment
system, the system operates on the application layer and usually makes
use of a telecommunications network for lower layers of the message
exchange.
