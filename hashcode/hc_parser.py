#!/usr/bin/env python3
# coding: utf-8

from . import evalfile, pexist, gob, fbasenoext, fbasename, rm_eol
from . import rlines, prtnice, reporter, dcopy
from typing import List, Tuple


@reporter("hc_parser.reader")
def reader(fields: List[Tuple[str, type]], filename: str, callback) -> dict:
    content = None or rlines(filename)
    if content is None:
        raise RuntimeError(
            f"couldn't process {filename}: may be empty or can not read")

    first_line = content[0].split(' ')
    if len(first_line) > len(fields):
        raise RuntimeError("You forgot to update the FIELDS definition in problem.py, parsed too many fields")
    if len(first_line) < len(fields):
        raise RuntimeError(f"You want too many fields ({len(fields)}) but the file has {len(first_line)} fields in its header")

    data = {
        fields[i][0]: fields[i][1](rm_eol(e)) for i,
        e in enumerate(first_line)
    }

    cdata = callback(dcopy(data), content[1:])
    data.update(cdata)

    return data


@reporter("hc_parser.saver")
def saver(fields: List[Tuple[str, type]], filename: str, callback) -> None:
    with open(f"parsed/{filename}", "w") as f:
        f.write(prtnice(reader(fields, f"tests/{filename}", callback)))


def save_all(fields: List[Tuple[str, type]], callback) -> None:
    print("Saving all...")
    for f in gob(f"tests/*.txt"):
        print(f"Exporting {f}...\r")
        saver(fields, fbasename(f), callback)
    print("\nDone!")


@reporter("hc_parser.generate_output")
def generate_output(data: dict, filename: str, algo_name: str, callback) -> None:
    # if we need data from the problem source
    og_file = load(filename)
    out = callback(og_file, data)

    content = str(len(data)) + '\n'
    content += ''.join(map(str, (line for line in out)))

    racine = fbasenoext(filename)
    with open(f"output/{racine}-{algo_name}.txt", "w") as f:
        f.write(content)


def load(filename: str) -> dict:
    return evalfile(f"parsed/{filename}")
