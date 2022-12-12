#!/usr/bin/env python3

import networkx as nx

from d12.s1 import get_map, init_graph


def gen_shortest_paths(g, m, end):
    ylen = len(m)
    xlen = len(m[0])

    for y in range(ylen):
        for x in range(xlen):
            if m[y][x] == 'a':
                try:
                    yield nx.shortest_path_length(g, source=(x, y), target=end) + 2
                except nx.exception.NetworkXNoPath:
                    pass


def main():
    m = get_map()
    g = nx.DiGraph()

    _, end = init_graph(g, m)

    return min(gen_shortest_paths(g, m, end))


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
