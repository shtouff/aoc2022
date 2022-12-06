#!/usr/bin/env python3
from d05.s1 import do_moves, crane9000


def main():
    return do_moves(crane9000)


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
