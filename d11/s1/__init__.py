import re
from dataclasses import dataclass
from typing import List, Callable


token_specification = [
    ('NUMBER',   r'[0-9]+'),
    ('OP',       r'[+\-*/]'),
    ('NEWLINE',  r'\n'),
    ('ID',       r'[A-Za-z]+'),
    ('SKIP',     r'[ :\t]+'),
    ('MISMATCH', r'.'),
]
token_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_specification))


@dataclass(frozen=False)
class Monkey:
    mid: int
    items: List[int]
    test_divider: int
    test_true: int
    test_false: int
    op: Callable[[int], int]
    inspected: int = 0


def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def build_operation(operator: str, operand: str):
    if operator == '+':
        f = addition
    elif operator == '*':
        f = multiplication

    if operand == 'old':
        def op(old):
            return f(old, old)
    else:
        def op(old):
            return f(old, int(operand))

    return op


def build_monkey(buff: str):
    mid = None
    items = []
    operand = operator = None
    test_divider = None
    test_true = test_false = None

    line_num = 1
    for m in token_regex.finditer(buff):
        kind = m.lastgroup
        val = m.group()

        if kind == 'NUMBER':
            if line_num == 1:
                mid = int(val)
            elif line_num == 2:
                items.append(int(val))
            elif line_num == 3:
                operand = val
            elif line_num == 4:
                test_divider = int(val)
            elif line_num == 5:
                test_true = int(val)
            elif line_num == 6:
                test_false = int(val)
        elif kind == 'NEWLINE':
            line_num += 1
        elif kind == 'OP':
            operator = val
        elif kind == 'ID':
            if operator and val == 'old':
                operand = 'old'

    return Monkey(
        mid=mid, items=items,
        op=build_operation(operator=operator, operand=operand),
        test_divider=test_divider, test_true=test_true, test_false=test_false,
    )


def gen_monkeys():
    with open('../input.txt') as _in:
        buff = []
        for line in _in:
            if line in ('', '\n'):
                yield build_monkey(''.join(buff))
                buff = []
            else:
                buff.append(line)
        yield build_monkey(''.join(buff))
