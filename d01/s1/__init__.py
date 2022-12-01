def gen_elves():
    with open("input.txt") as _in:
        elf = 0
        while True:
            line = _in.readline()
            if line == '':
                break
            elif line == '\n':
                yield elf
                elf = 0
            else:
                elf += int(line.rstrip())

