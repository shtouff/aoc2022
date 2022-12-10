from typing import Generator


def gen_elves() -> Generator[int, None, None]:
    with open("../input.txt") as _in:
        elf = 0
        for line in (e.rstrip('\n') for e in _in):
            if line == '':
                yield elf
                elf = 0
            else:
                elf += int(line)
