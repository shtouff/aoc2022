from typing import Callable

shape_scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

shape_equivs = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

wins = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}


def compute_ideal_score(line: str) -> int:
    his = line[0]
    mine = line[2]
    mine = shape_equivs[mine]
    score = shape_scores[mine]

    if his == mine:
        return score + 3
    elif mine == wins[his]:
        return score + 6
    else:
        return score + 0


def gen_matches(compute_score: Callable[[str], int]):
    with open("input.txt") as _in:
        while (line := _in.readline()) != '':
            yield compute_score(line)
