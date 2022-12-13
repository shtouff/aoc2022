#!/usr/bin/env python3
from functools import cmp_to_key

from d13.s1 import gen_pairs, cmp_msgs


def main():
    packets = []
    for e1, e2 in gen_pairs():
        packets.extend([eval(e1), eval(e2)])

    packets.extend([[[2]], [[6]]])
    packets.sort(key=cmp_to_key(cmp_msgs))

    dividers = [p[0] for p in enumerate(packets, 1) if p[1] in ([[2]], [[6]])]
    return dividers[0] * dividers[1]


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
