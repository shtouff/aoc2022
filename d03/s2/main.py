#!/usr/bin/env python3
from d03.s1 import get_prio, get_common_type


def gen_runsacks():
    with open("input.txt") as _in:
        sets = []
        while (rs := _in.readline()) != '':
            rs = rs.rstrip('\n')
            sets.append(set(rs))

            if len(sets) == 3:
                yield get_prio(get_common_type(*sets))
                sets = []


print(sum(gen_runsacks()))
