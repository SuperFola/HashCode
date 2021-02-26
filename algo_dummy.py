#!/usr/bin/env python3
# coding: utf-8

from hashcode import reporter, fbasename


@reporter(__file__)
def run(filename: str, data: dict):
    print(f"Running {fbasename(__file__)} on {filename}...")

    out = {}

    # dummy
    for k, v in data.items():
        out[k] = v

    return out