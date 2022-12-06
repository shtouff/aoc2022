import itertools


def stop_after_n_distinct(fname: str, n: int) -> int:
    with open(fname) as _in:
        line = _in.readline()

    streams = [line[i:] for i in range(n)]
    window = zip(*streams)

    for i, candidate in zip(itertools.count(), window):
        if len(set(candidate)) == n:
            return i + n
