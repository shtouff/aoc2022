import re
from typing import Generator

from treelib import Tree


cd_regex = re.compile(r'^\$ cd (/|\.\.|.+)')
file_regex = re.compile(r'^(dir|[0-9]+) (.+)')


def gen_tree() -> Tree:
    cwd = []
    tree = Tree()
    tree.create_node("/", "/", data=None)
    with open('../input.txt') as _in:
        for line in (e.rstrip('\n') for e in _in):
            if m := cd_regex.match(line):
                if m[1] == '/':
                    cwd = []
                elif m[1] == '..':
                    cwd.pop()
                else:
                    cwd.append(m[1])
            elif m := file_regex.match(line):
                parent = '/' + '/'.join(cwd)
                if parent.endswith('/'):
                    node = parent + m[2]
                else:
                    node = parent + '/' + m[2]
                if m[1] == 'dir':
                    tree.create_node(m[2], node, parent=parent, data=None)
                else:
                    tree.create_node(m[2], node, parent=parent, data=int(m[1]))

    return tree


def tree_size(tree: Tree) -> int:
    return sum([tree[node].data for node in tree.expand_tree() if tree[node].data is not None])


def gen_small_dirs(tree: Tree) -> Generator[int, None, None]:
    for node in tree.expand_tree():
        if tree[node].data is None:
            if (size := tree_size(tree.subtree(node))) < 100_000:
                yield size
