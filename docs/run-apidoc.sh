#!/bin/sh

# Runs spinhx-apidoc to generate the Tapestry documentation. Running
# "make html" after this script is necessary as well.

# FIXME: Creates also .rst for Django migrations which is spurious
# (and they're excluded in Sphinx configuration).

sphinx-apidoc -f -M -o ./api ../tapestry
