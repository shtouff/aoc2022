#!/usr/bin/env python3
from typing import Generator

from d04.s1 import parse_assignments


def gen_overlapped_assignments() -> Generator[str, None, None]:
    with open('../input.txt') as _in:
        for line in _in:
            one, two = parse_assignments(line)
            if not one.isdisjoint(two):
                yield line


def main():
    return len(list(gen_overlapped_assignments()))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
