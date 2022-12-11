#!/usr/bin/env python3
from functools import reduce

from d11.s1 import gen_monkeys


def main():
    monkeys = list(gen_monkeys())
    gcd = reduce(lambda a, b: a*b, [mk.test_divider for mk in monkeys])

    for _ in range(10_000):
        for mk in monkeys:
            for item in mk.items:
                mk.inspected += 1
                wlvl = mk.op(item)

                if wlvl % mk.test_divider == 0:
                    monkeys[mk.test_true].items.append(wlvl % gcd)
                else:
                    monkeys[mk.test_false].items.append(wlvl % gcd)

            mk.items = []

    inspected = [mk.inspected for mk in monkeys]
    mosts = sorted(inspected)
    return mosts[-1] * mosts[-2]


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
