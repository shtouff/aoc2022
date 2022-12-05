import re
from typing import List, Generator, Tuple, Callable


def build_stack_regex():
    chunk = r'(\[[A-Z]\]|   )'
    chunk_list = [chunk] * 9
    res = r'^' + r' '.join(chunk_list)
    return re.compile(res)


stack_regex = build_stack_regex()
move_regex = re.compile(r'^move ([0-9]+) from ([0-9]) to ([0-9])')


def get_stacks(_in) -> List[List[str]]:
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in (e.rstrip('\n') for e in _in):
        if m := stack_regex.match(line):
            for i in range(9):
                if not m[i+1] == '   ':
                    stacks[i].insert(0, m[i+1][1])
        else:
            return stacks


def gen_moves(_in) -> Generator[Tuple[int, int, int], None, None]:
    for line in (e.rstrip('\n') for e in _in):
        if m := move_regex.match(line):
            yield int(m[1]), int(m[2]), int(m[3])


def crane9000(count, src, dest):
    for i in range(count):
        crate = src.pop()
        dest.append(crate)


def do_moves(crane: Callable[[int, List[str], List[str]], None]):
    with open('input.txt') as _in:
        stacks = get_stacks(_in)
        for count, src, dest in gen_moves(_in):
            crane(count, stacks[src - 1], stacks[dest - 1])

        for s in stacks:
            print(s[-1], end='')
        print()
