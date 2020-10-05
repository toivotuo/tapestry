TAPESTRY - A PAYMENTS ROUTER
============================

Tapestry is a set of experiments in developing a multi-scheme
"clearing and settlement mechanism" (CSM) for account to account
payments between "payment service providers" (PSP) such as banks and
other financial institutions. Tapestry is not production quality
software. It is best understood in the tradition of operating systems
developed to teach computer science concepts. Minix_ and Xv6_ are
examples of Unix-like teaching operating systems.

.. _Minix: https://www.minix3.org/
.. _Xv6: https://pdos.csail.mit.edu/6.828/2020/xv6.html

What's in the name? See "Star Trek: TNG (S6E15_)".

.. _S6E15: https://memory-alpha.fandom.com/wiki/Tapestry_(episode)

.. toctree::
   :maxdepth: 2
   :caption: System overview

   introduction.rst
   running.rst
   design.rst
   implementation.rst
   development.rst
   related-work.rst

.. toctree::
   :maxdepth: 2
   :caption: System modules

   clearer.rst
   settler.rst
   router.rst
   impsepa.rst
   impsic.rst

.. automodule:: tapestry
   :members:

Indices
-------

* :ref:`modindex` - Code modules
* :ref:`genindex` - Code index
