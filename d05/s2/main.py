#!/usr/bin/env python3
from d05.s1 import do_moves


def crane9001(count, src, dest):
    crates = src[-count:]
    del src[-count:]
    dest.extend(crates)


stacks = do_moves(crane9001)
