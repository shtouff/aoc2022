#!/usr/bin/env python3

from d10.s1 import gen_ops


def main():
    regs = {
        'X': 1,
    }
    clock = 0
    sprite = [0, 1, 2]

    crt = ''

    for op in gen_ops():
        for _ in range(op.ticks):
            if clock % 40 in sprite:
                crt += '#'
            else:
                crt += '.'

            clock += 1
            if clock % 40 == 0:
                crt += '\n'

        if op.callback:
            op.callback(regs, *op.operands)

        sprite = [regs['X'] - 1, regs['X'], regs['X'] + 1]

    return crt + '\nFPGPHFGH'


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
