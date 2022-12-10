#!/usr/bin/env python3
from d06.s1 import stop_after_n_distinct


def main():
    return stop_after_n_distinct('../input.txt', 14)


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
