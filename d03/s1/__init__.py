from typing import Set

A = ord('A')
a = ord('a')
assert a > A


def get_prio(c: str) -> int:
    if (o := ord(c)) >= a:
        return o - a + 27
    else:
        return o - A + 1


def get_common_type(*sets: Set[str]) -> str:
    return ''.join(sets[0].intersection(*sets[1:]))

