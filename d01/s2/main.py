#!/usr/bin/env python3
from d01.s1 import gen_elves


def main():
    return sum(sorted(gen_elves())[-3:])


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
