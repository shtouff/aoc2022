from typing import Set


def get_prio(c: str) -> int:
    o = ord(c)
    if 65 <= o <= 90:
        return o - 65 + 27
    elif 97 <= o <= 122:
        return o - 97 + 1


def get_common_type(*sets: Set[str]) -> str:
    return ''.join(sets[0].intersection(*sets[1:]))

