import re
from dataclasses import dataclass
from typing import List, Callable


op_regex = re.compile(r'^(noop|addx) ?(-?[0-9]+)?')


def do_addx(regs, *operands):
    regs['X'] += int(operands[0])


@dataclass
class Op:
    operands: List[str]
    ticks: int = 1
    callback: Callable[[str, ...], None] = None


@dataclass
class noop(Op):
    pass


@dataclass
class addx(Op):
    ticks: int = 2
    callback: Callable[[str, ...], None] = do_addx


instructions = {
    'noop': noop,
    'addx': addx,
}


def gen_ops():
    with open('../input.txt') as _in:
        for line in (e.rstrip('\n') for e in _in):
            if m := op_regex.match(line):
                yield instructions[m.groups()[0]](operands=m.groups()[1:])

