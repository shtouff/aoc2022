#!/usr/bin/env python3
from typing import Generator

from d03.s1 import get_common_type, get_prio


def gen_runsacks() -> Generator[int, None, None]:
    with open("input.txt") as _in:
        for rs in (e.rstrip('\n') for e in _in):
            cs = len(rs) // 2
            yield get_prio(get_common_type(set(rs[0:cs]), set(rs[cs:])))


print(sum(gen_runsacks()))
