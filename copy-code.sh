#!/bin/sh

# Copy code used in the thesis to the repository containing the LyX
# documents where the code is included from.

TARGET2="../repo/tapestry/code"

cat<<EOF | while read f
./scripts/sepa-csm-pricing-comparison.py
./tapestry/scheme-messages.yaml
EOF
do
    echo $f
    grep -v FIXME $f | cat -s > ${TARGET2}/`basename ${f}`
done
