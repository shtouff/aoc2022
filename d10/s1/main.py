#!/usr/bin/env python3
from d10.s1 import gen_ops


def main():
    regs = {
        'X': 1,
    }
    clock = 0
    result = 0

    for op in gen_ops():
        for _ in range(op.ticks):
            clock += 1
            if clock in [20, 60, 100, 140, 180, 220]:
                result += clock * regs['X']

        if op.callback:
            op.callback(regs, *op.operands)

    return result


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
