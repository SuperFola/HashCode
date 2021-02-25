#!/usr/bin/env python3
# coding: utf-8

import hc_parser
from reporter import reporter


@reporter(__file__)
def run(filename):
    print(f"Running {__file__} on {filename}...")

    out = {}
    data = hc_parser.load(filename)

    hc_parser.generate_output(out, filename)
    return 0