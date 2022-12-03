#!/usr/bin/env python3
from d02.s1 import gen_matches
from d02.s2 import compute_wanted_score

print(sum(gen_matches(compute_wanted_score)))
