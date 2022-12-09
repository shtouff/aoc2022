#!/usr/bin/env python3
from typing import Tuple, Set, List

from d09.s1 import move_head, adjacent, move_tail, gen_moves


def do_move(h: List[int], t: List[int], direction: str, steps: int, visited: Set[Tuple[int]]):
    for _ in range(steps):
        move_head(h, direction)
        if not adjacent(h, t):
            move_tail(h, t)
            visited.add(tuple(t))


def main():
    h, t = ([0, 0], [0, 0])
    visited = set()
    visited.add(tuple(t))

    for direction, steps in gen_moves():
        do_move(h, t, direction, steps, visited)

    return len(visited)


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
