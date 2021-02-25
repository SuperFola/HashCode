#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import glob

import hc_parser
from hc_short import *

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
    if len(glob.glob("tests/*.txt")) != len(glob.glob("parsed/*.txt")) or \
        "-f" in args or "--force" in args:
        # run only if needed
        hc_parser.save_all()
        return 0

    if len(args) == 0:
        print("Missing argument: algorithm name")
        return -1

    algo_name = args[0]
    if not pexist(f"{algo_name}.py"):
        print(f"Couldn't find {algo_name}.py, check that you're in the right folder")
        return -1
    exec(f"import {algo_name}", G(), L())
    for le in args[1:] or "abcdef":
        exec(f"{algo_name}.run('{le}.txt')", G(), L())

    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))