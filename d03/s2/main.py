#!/usr/bin/env python3
from typing import Generator

from d03.s1 import get_prio, get_common_type


def gen_runsacks() -> Generator[int, None, None]:
    with open('../input.txt') as _in:
        sets = []
        for rs in (e.rstrip('\n') for e in _in):
            sets.append(set(rs))

            if len(sets) == 3:
                yield get_prio(get_common_type(*sets))
                sets = []


def main():
    return sum(gen_runsacks())


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
