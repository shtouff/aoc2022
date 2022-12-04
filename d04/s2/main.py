#!/usr/bin/env python3
from typing import Generator

from d04.s1 import parse_assignments


def gen_overlapped_assignments() -> Generator[str, None, None]:
    with open('input.txt') as _in:
        for line in _in:
            one, two = parse_assignments(line)
            if not one.isdisjoint(two):
                yield line


print(len(list(gen_overlapped_assignments())))
