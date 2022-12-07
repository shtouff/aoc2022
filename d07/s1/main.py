#!/usr/bin/env python3
from d07.s1 import gen_tree, gen_small_dirs


def main():
    tree = gen_tree()
    return sum(gen_small_dirs(tree))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
