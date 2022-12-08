#!/usr/bin/env python3
from typing import Generator

import numpy as np


def scenic_score(x: int, y: int, grid: np.array) -> int:
    if x in (0, len(grid) - 1) or y in (0, len(grid) - 1):
        return 0  # at least one of the 4 viewing distances equals 0

    v = grid[y, x]
    top = grid[0:y, x:x + 1].flatten()
    bottom = grid[y + 1:, x:x + 1].flatten()
    left = grid[y:y + 1, 0:x].flatten()
    right = grid[y:y + 1, x + 1:].flatten()

    score = 1
    for vector in reversed(top), bottom, reversed(left), right:
        vdistance = 0
        for h in vector:
            vdistance += 1
            if h >= v:
                break
        score *= vdistance

    return score


def gen_scores(grid: np.array) -> Generator[int, None, None]:
    for y in range(len(grid)):
        for x in range(len(grid)):
            yield scenic_score(x, y, grid)


def main():
    grid = []
    with open('input.txt') as _in:
        for line in (e.rstrip('\n') for e in _in):
            grid.append([int(e) for e in line])
    grid = np.array(grid)
    return max(gen_scores(grid))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
