#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import glob

from hashcode import hc_parser, G, L, pexist, gob
from problem import FIELDS, parse_input, generate_output


try:
    import numpy as np
    import psutil
except ModuleNotFoundError:
    import pip
    pip.main("install numpy psutil".split())
    exec("import numpy as np", G(), L())


HELP_MSG = """Hello World!

python3 main.py ALGO ARGUMENTS... [OPTIONS]

ALGO
    n   algorithm name

ARGUMENTS
    a   to run on the a.txt file
    b   to run on the b.txt file
    c   to run on the c.txt file
    d   to run on the d.txt file
    e   to run on the e.txt file
    f   to run on the f.txt file

    nothing
        run everything

    can cumulate arguments, order not important:
        python3 main.py algo_dummy a c b d

OPTIONS
    -h, --help    print this
    -f, --force   force regeneration of the parsed tests
"""


def main(*args):
    if "-h" in args or "--help" in args:
        print(HELP_MSG)
        return 0

    # read all .txt files and convert them to python dict, then save that to
    # ./parsed/filename.txt
    if len(gob("tests/*.txt")) != len(gob("parsed/*.txt")
                                      ) or "-f" in args or "--force" in args:
        # run only if needed
        hc_parser.save_all(FIELDS, parse_input)
        return 0

    if len(args) == 0:
        print("Missing argument: algorithm name")
        return -1

    algo_name = args[0]
    if not pexist(f"{algo_name}.py"):
        print(
            f"Couldn't find {algo_name}.py, check that you're in the right folder")
        return -1
    exec(f"import {algo_name}", G(), L())
    func = eval(f"{algo_name}.run", G(), L())
    for le in (args[1:] or "abcdef"):
        try:
            fname = f"{le}.txt"
            print(f"Running {algo_name} on {fname}...")
            output = func(fname, hc_parser.load(fname))
            hc_parser.generate_output(output, fname, algo_name, generate_output)
        except Exception as e:
            print(f"Error when running {algo_name}({le}): {e}")

    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
