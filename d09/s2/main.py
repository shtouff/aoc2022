#!/usr/bin/env python3
from typing import Tuple, Set, List

from d09.s1 import move_head, adjacent, move_tail, gen_moves


def do_move(knots: List[List[int]], direction: str, steps: int, visited: Set[Tuple[int]]):
    for _ in range(steps):
        move_head(knots[0], direction)

        for h, t in zip(knots, knots[1:]):
            if not adjacent(h, t):
                move_tail(h, t)
        visited.add(tuple(knots[-1]))


def main():
    knots = [[0, 0] for _ in range(10)]
    visited = set()
    visited.add(tuple(knots[-1]))

    for direction, steps in gen_moves():
        do_move(knots, direction, steps, visited)

    return len(visited)


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
