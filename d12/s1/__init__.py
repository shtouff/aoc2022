from typing import List, Tuple, Optional

import networkx as nx


def get_map() -> List[List[str]]:
    m = []
    with open('../input.txt') as _in:
        for line in (e.rstrip('\n') for e in _in):
            m.append(list(line))

    return m


def add_edges(g: nx.DiGraph, m: List[List[str]], x: int, y: int):
    ylen = len(m)
    xlen = len(m[0])
    ev_node = ord(m[y][x])

    u = (x, y - 1) if y > 0 else None
    d = (x, y + 1) if y < ylen - 1 else None
    l = (x - 1, y) if x > 0 else None
    r = (x + 1, y) if x < xlen - 1 else None
    for neigh in (n for n in (u, d, l, r) if n):
        ev_neigh = ord(m[neigh[1]][neigh[0]])

        if ev_node > ev_neigh:
            g.add_edge((x, y), neigh)
            if ev_node == ev_neigh + 1:
                g.add_edge(neigh, (x, y))
        elif ev_node < ev_neigh:
            g.add_edge(neigh, (x, y))
            if ev_node + 1 == ev_neigh:
                g.add_edge((x, y), neigh)
        else:
            g.add_edge((x, y), neigh)
            g.add_edge(neigh, (x, y))


def init_graph(g: nx.DiGraph, m: List[List[str]]) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
    ylen = len(m)
    xlen = len(m[0])
    start = end = None

    for y in range(ylen):
        for x in range(xlen):
            if m[y][x] == 'S':
                start = (x, y)
                m[y][x] = 'a'
            elif m[y][x] == 'E':
                end = (x, y)
                m[y][x] = 'z'

            add_edges(g, m, x, y)
    return start, end
