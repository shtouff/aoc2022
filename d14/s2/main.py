#!/usr/bin/env python3
from typing import Tuple, Optional

from d14.s1 import init_map
# from d14.s1 import display_map


def pour_sand(m: dict, ymax: int) -> Optional[Tuple[int, int]]:
    x = 500
    y = 0

    while y <= ymax:
        if y + 1 == ymax:
            for pos in (x, y + 1), (x - 1, y + 1), (x + 1, y + 1):  # materialize a segment of the virtual bottom
                m[pos] = '#'

        for pos in (x, y + 1), (x - 1, y + 1), (x + 1, y + 1):  # down, down + left, down + right
            if pos not in m:
                x, y = pos
                break

        if (x, y) != pos:  # if we couldn't move more, we're at rest
            break

    m[(x, y)] = 'o'
    return x, y


def main():
    cave_map = init_map(500, 0)
    # display_map(cave_map)

    resting_units = 0
    ymax = max([c[1] for c in cave_map.keys()])

    while pour_sand(cave_map, ymax + 2) and cave_map[(500, 0)] != 'o':
        resting_units += 1
        # if resting_units % 10 == 0:
        #     display_map(cave_map)

    # display_map(cave_map)
    return resting_units + 1


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
