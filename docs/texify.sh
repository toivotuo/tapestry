#!/bin/sh

# Convert selected files to LaTeX and copy for inclusion in the
# appendices of the TLBOP LyX document.

cat <<EOF | while read f
introduction
design
implementation
development
ledger
router
clearer
settler
fex
imp
impsepa
impsic
imp8583
EOF
do
    echo ${f}
    pandoc -o ~/tlbop/repo/tapestry/${f}.tex ${f}.rst
done
