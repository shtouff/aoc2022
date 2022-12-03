from d02.s1 import wins, shape_scores

looses = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}


def compute_wanted_score(line: str) -> int:
    his = line[0]
    mine = line[2]
    score = 0

    if mine == 'X':
        mine = looses[his]
    elif mine == 'Y':
        mine = his
        score = 3
    elif mine == 'Z':
        mine = wins[his]
        score = 6

    return score + shape_scores[mine]
