#!/usr/bin/env python3
import math

from d11.s1 import gen_monkeys


def main():
    monkeys = list(gen_monkeys())
    for _ in range(20):
        for mk in monkeys:
            for item in mk.items:
                mk.inspected += 1
                wlvl = mk.op(item)
                wlvl = math.floor(wlvl / 3)

                if wlvl % mk.test_divider == 0:
                    monkeys[mk.test_true].items.append(wlvl)
                else:
                    monkeys[mk.test_false].items.append(wlvl)

            mk.items = []

    mosts = sorted([mk.inspected for mk in monkeys])
    return mosts[-1] * mosts[-2]


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
