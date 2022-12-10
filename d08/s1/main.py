#!/usr/bin/env python3
from typing import Generator

import numpy as np


def is_visible(x: int, y: int, grid: np.array) -> bool:
    if x in (0, len(grid) - 1) or y in (0, len(grid) - 1):
        return True

    v = grid[y, x]
    top = grid[0:y, x:x + 1].flatten()
    bottom = grid[y + 1:, x:x + 1].flatten()
    left = grid[y:y + 1, 0:x].flatten()
    right = grid[y:y + 1, x + 1:].flatten()

    return max(top) < v or max(bottom) < v or max(left) < v or max(right) < v


def gen_visibles(grid: np.array) -> Generator[int, None, None]:
    for y in range(len(grid)):
        for x in range(len(grid)):
            if is_visible(x, y, grid):
                yield 1


def main():
    grid = []
    with open('../input.txt') as _in:
        for line in (e.rstrip('\n') for e in _in):
            grid.append([int(e) for e in line])
    grid = np.array(grid)
    return sum(gen_visibles(grid))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
