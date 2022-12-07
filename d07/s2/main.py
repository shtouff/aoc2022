#!/usr/bin/env python3
from typing import Generator

from treelib import Tree

from d07.s1 import gen_tree, tree_size


def gen_big_dirs(tree, n: int) -> Generator[int, None, None]:
    for node in tree.expand_tree(mode=Tree.WIDTH):
        if tree[node].data is None:
            if (size := tree_size(tree.subtree(node))) >= n:
                yield size


def main():
    tree = gen_tree()
    total = tree_size(tree)
    disk = 70_000_000
    needed = 30_000_000

    return min(gen_big_dirs(tree, total - (disk - needed)))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
