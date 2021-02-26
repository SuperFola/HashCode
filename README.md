# HashCode template

## To modify

- modify the problem parser (in `problem.py`) to your needs (from the INPUT and OUTPUT specifications)
- create `algo_name.py`, with algo_name the name of your algorithm
    - run it with `main.py algo_name` to run on all files, or `main.py algo_name a b` to run on a and b problems

## Adding an algorithm

Create a file `algo_name.py` alongside `main.py`, base content looks like this:

```python
#!/usr/bin/env python3
# coding: utf-8

from hashcode import reporter


@reporter(__file__)
def run(filename: str, data: dict):
    out = {}

    # your code is here

    return out
```

## Adding the INPUT and OUTPUT parsers

Your parsers should be written in `problem.py`.

### INPUT

The `parse_input` method will be given the header as a dict, defined by the `FIELDS` which is a mapping `field name => type` (you can choose whatever field name you want, but **the type has to be exactly what you want**).

The `parse_input` method is also given the rest of the lines of the file (without the first line) and should return what it parsed from those lines as a dict. **Do not include the header** it will be include by the caller.

### OUTPUT

The `generate_output` method will be given the original data parsed before for the problem, the dictionnary returned by the parser. It will also be given the solution your algorithm generated **as a dict**.

It should return a list of string, each one being an element of the problem.

**Then the parser will write at the top of the file the number of components you generated**. The first line of an output file for the google hashcode is **always** the number of solution, thus it should be carefully designed in your generate_output to return the right number of elements.