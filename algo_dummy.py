#!/usr/bin/env python3
# coding: utf-8

import hc_parser
from reporter import reporter
from hc_short import *


@reporter(__file__)
def run(filename):
    print(f"Running {fbasename(__file__)} on {filename}...")

    out = {}
    data = hc_parser.load(filename)

    # dummy
    for k, v in data.items():
        out[k] = v

    return out