#!/usr/bin/env python3
import networkx as nx

from d12.s1 import get_map, init_graph


def main():
    m = get_map()
    g = nx.DiGraph()
    start, end = init_graph(g, m)

    return nx.shortest_path_length(g, source=start, target=end) + 2


if __name__ == '__main__':
    from timeit import timeit
    print(str(main()) + ' time: ' + str(timeit("main()", setup="from __main__ import main", number=1)))
