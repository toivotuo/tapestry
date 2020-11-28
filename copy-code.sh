#!/bin/sh

# Copy code used in the thesis to the repository containing the LyX
# documents where the code is included from.

TARGET2="../repo/tapestry/code"

cat<<EOF | while read src dst
./scripts/sepa-csm-pricing-comparison.py sepa-csm-pricing-comparison.py
./tapestry/scheme-messages.yaml scheme-messages.yaml
./tapestry/router/models.py router-models.py
./tapestry/router/management/commands/import_separouting.py import-separouting.py
./tapestry/router/management/commands/import_scldirectory.py import-scldirectory.py
./tapestry/router/management/commands/import_tipsreach.py import-tipsreach.py
EOF
do
    echo $dst
    grep -v FIXME $src | cat -s > ${TARGET2}/${dst}
done
