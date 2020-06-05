#!python3

# Small test script to read and write Avro files.

import json
from fastavro import writer, reader, parse_schema

schemafile = "Payment.avsc"
datafile = "test.avro"

payments = [
    {
        "debtor": "Senna Koiranen",
        "debtor_iban": "GR1601101050000010547023795",
        "creditor": "Jean-Luc Picard",
        "creditor_iban": "BE31435411161155",
        "amount": "42.00",
        "currency": "EUR",
    },
]

schema = parse_schema(json.load(open(schemafile, "rb")))


# Write an Avro file

with open(datafile, 'wb') as fout:
    writer(fout, schema, payments)

# Read an Avro file

with open(datafile, 'rb') as fin:
    for p in reader(fin):
        print(p)
