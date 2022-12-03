#!/usr/bin/env python3
from d01.s1 import gen_elves

print(sum(sorted(gen_elves())[-3:]))
