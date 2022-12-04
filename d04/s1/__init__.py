import re
from typing import Tuple, Set

regex = re.compile(r'([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)')


def parse_assignments(line: str) -> Tuple[Set[str], Set[str]]:
    m = regex.match(line)
    return set(range(int(m[1]), 1 + int(m[2]))), set(range(int(m[3]), 1 + int(m[4])))
