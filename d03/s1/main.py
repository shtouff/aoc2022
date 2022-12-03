#!/usr/bin/env python3
from d03.s1 import get_common_type, get_prio


def gen_runsacks():
    with open("input.txt") as _in:
        while (rs := _in.readline()) != '':
            rs = rs.rstrip('\n')
            cs = len(rs) // 2
            yield get_prio(get_common_type(set(rs[0:cs]), set(rs[cs:])))


print(sum(gen_runsacks()))
