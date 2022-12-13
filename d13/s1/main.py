#!/usr/bin/env python3
from d13.s1 import gen_pairs, cmp_msgs


def main():
    results = []
    for e1, e2 in gen_pairs():
        results.append(cmp_msgs(eval(e1), eval(e2)))

    return sum([t[0] for t in enumerate(results, 1) if t[1] <= 0])


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
