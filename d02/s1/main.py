#!/usr/bin/env python3
from d02.s1 import gen_matches, compute_ideal_score


def main():
    return sum(gen_matches(compute_ideal_score))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
