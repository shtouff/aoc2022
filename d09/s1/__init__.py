import re
from typing import Generator, Tuple, List


move_regex = re.compile(r'^([UDLR]) ([0-9]+)')


def gen_moves() -> Generator[Tuple[str, int], None, None]:
    with open('../input.txt') as _in:
        for move in (line.rstrip('\n') for line in _in):
            if m := move_regex.match(move):
                yield m[1], int(m[2])


def adjacent(h: List[int], t: List[int]) -> bool:
    norm = abs(h[0] - t[0]) + abs(h[1] - t[1])

    if norm < 2:
        return True
    elif norm == 2:  # are we diagonally adjacent ?
        return not (h[0] == t[0] or h[1] == t[1])
    else:
        return False


def move_tail(h: List[int], t: List[int]):
    if h[0] == t[0]:
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
    elif h[1] == t[1]:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
    else:  # diagonal move, update both coords
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1


def move_head(h: List[int], direction: str):
    if direction == 'R':
        h[0] += 1
    elif direction == 'L':
        h[0] -= 1
    elif direction == 'D':
        h[1] += 1
    elif direction == 'U':
        h[1] -= 1
