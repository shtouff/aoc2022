#!/usr/bin/env python3
from typing import Generator

from d03.s1 import get_prio, get_common_type


def gen_runsacks() -> Generator[int, None, None]:
    with open('input.txt') as _in:
        sets = []
        for rs in (e.rstrip('\n') for e in _in):
            sets.append(set(rs))

            if len(sets) == 3:
                yield get_prio(get_common_type(*sets))
                sets = []


print(sum(gen_runsacks()))
