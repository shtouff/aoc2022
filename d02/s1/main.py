#!/usr/bin/env python3
from d02.s1 import gen_matches, compute_ideal_score

print(sum(gen_matches(compute_ideal_score)))
