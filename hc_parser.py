#!/usr/bin/env python3
# coding: utf-8

import os
from hc_short import *
from reporter import reporter


FIELD_1 = "deadline"
FIELD_2 = "intersection_count"
FIELD_3 = "street_count"
FIELD_4 = "car_count"
FIELD_5 = "bonus_per_car"

FIELDS = [FIELD_1, FIELD_2, FIELD_3, FIELD_4, FIELD_5]


@reporter("hc_parser.reader")
def reader(filename):
    content = None or rlines(filename)
    if content is None:
        raise RuntimeError(f"couldn't process {filename}: may be empty or can not read")

    data = {
        FIELDS[i]: rm_eol(e) for i, e in enumerate(content[0].split(' '))
    }

    # TODO

    return data


@reporter("hc_parser.saver")
def saver(filename):
    with open(f"parsed/{filename}", "w") as f:
        f.write(prtnice(reader(f"tests/{filename}")))


def save_all():
    print("Saving all...")
    for f in gob(f"tests/*.txt"):
        print(f"Exporting {f}...\r")
        saver(fbasename(f))
    print("\nDone!")


@reporter("hc_parser.generate_output")
def generate_output(data, filename):
    out = []

    content = str(len(data)) + '\n'
    content += ''.join(map(str, (line for line in out)))

    racine = fbasenoext(filename)
    with open(f"output/{racine}-{len(gob(f'output/{racine}-*'))}", "w") as f:
        f.write(content)


def load(filename):
    return evalfile(f"parsed/{filename}")
