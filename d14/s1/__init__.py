import re
from typing import Tuple, Optional, List, Generator, Dict

coords_regex = re.compile(r'([0-9]+),([0-9]+)')


def gen_rock_lines() -> Generator[List[Tuple[int, int]], None, None]:
    with open('../input.txt') as _in:
        for line in (e.rstrip('\n') for e in _in):
            rock_line = []
            for m in coords_regex.finditer(line):
                rock_line.append((int(m[1]), int(m[2])))
            yield rock_line


def init_map(x: int, y: int) -> Dict[Tuple[int, int], str]:
    cave_map = {
        (x, y): '+'
    }

    for line in gen_rock_lines():
        for c1, c2 in zip(line, line[1:]):
            cave_map[c1] = '#'
            cave_map[c2] = '#'
            if c1[0] == c2[0]:
                ymax = max([c1[1], c2[1]])
                ymin = min([c1[1], c2[1]])
                for y in range(ymin, ymax + 1):
                    cave_map[(c1[0]), y] = '#'
            elif c1[1] == c2[1]:
                xmax = max([c1[0], c2[0]])
                xmin = min([c1[0], c2[0]])
                for x in range(xmin, xmax + 1):
                    cave_map[(x, c1[1])] = '#'

    return cave_map


def display_map(m: dict):
    print('CAVE MAP:')
    for v in map_as_matrix(m):
        print(''.join(v))


def map_as_matrix(m: dict):
    a = []
    xmax = max([c[0] for c in m.keys()])
    xmin = min([c[0] for c in m.keys()])
    ymax = max([c[1] for c in m.keys()])

    for y in range(ymax + 1):
        a.append([])
        for x in range(xmin, xmax + 1):
            if (x, y) in m:
                a[y].append(m[(x, y)])
            else:
                a[y].append('.')
    return a
