from itertools import zip_longest
from typing import Tuple, Generator, Any, List


def gen_pairs() -> Generator[Tuple[str, str], None, None]:
    with open('../input.txt') as _in:
        first = None
        for line in (e.rstrip('\n') for e in _in):
            if line == '':
                continue
            if first is None:
                first = line
            else:
                yield first, line
                first = None


def cmp_msgs(msg1: List[Any], msg2: List[Any]):
    for e1, e2 in zip_longest(msg1, msg2):
        if type(e1) == type(e2) == int:
            if e2 < e1:
                return 1
            elif e2 > e1:
                return -1
        elif e1 is None:
            return -1
        elif e2 is None:
            return 1
        else:
            if type(e1) == int:
                e1 = [e1]
            elif type(e2) == int:
                e2 = [e2]
            if (ret := cmp_msgs(e1, e2)) == 0:
                continue
            else:
                return ret

    return 0

