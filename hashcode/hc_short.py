#!/usr/bin/env python3
# coding: utf-8

G = globals
L = locals

import glob
# shortcut to glob.glob
gob = lambda path: glob.glob(path)

import os
# check if file/path exists
pexist = lambda path: os.path.exists(path)
# get the file basename from a path
fbasename = lambda path: os.path.basename(path)
# get the file basename from a path without the extension
fbasenoext = lambda path: fbasename(path).split('.')[0]

# read lines from a file as a list of strings, 1 per line
def rlines(path: str):
    with open(path, "r") as f:
        return f.readlines()

# evaluate the object in a file and return the object
def evalfile(path: str):
    with open(path, "r") as f:
        return eval(f.read())

import pprint
# nice python object printing, returns as string
prtnice = lambda obj: pprint.pformat(obj, indent=4, width=120)

from copy import deepcopy
# shortcut to deepcopy an object
dcopy = deepcopy

rm_eol = lambda s: s.replace('\n', '')

# ensure that a value stays in given bounds
clamp = lambda val, minval, maxval: max(min(val, maxval), minval)

# given a list of elements, output a dict of element => count
count_to_dict = lambda lst: {n: lst.count(n) for n in set(lst)}