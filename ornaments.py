from collections import defaultdict

from utils import exp_weights, weighted_choice


REPLACE = defaultdict(dict)

REPLACE[16]['options'] = [
    [12, 4],
    [(12, 2), 2],
    [(12, 3), 1],
    [(12, 2), 1, 1],
    [12, 2, 2],
    [12, 1, 1, 1, 1],
    [(12, 1), 1, 1, 1],
    [(8, 3), 1, 1, 1, 1, 1],
    [(8, 2), 2, 2, 2],
    [8, 4, 4],
    [8, 2, 2, 2, 2],
    [(8, 3), 1, 4],
    [(8, 2), 1, 1, 4],
    [(8, 2), 2, 4],
    [12, 2, 1, 1],
    [1, (3, 12)],
    [2, (2, 12)],
    [1, 1, (2, 12)],
    [2, 2, 12],
    [1, 1, 1, (1, 12)],
    [1, 1, 1, 1, 12],

]

REPLACE[12]['options'] = [
    [8, 4],
    [(8, 2), 2],
    [(8, 3), 1],
    [(8, 2), 1, 1],
    [8, 1, 1, 1, 1],
    [8, 2, 2],
    [(4, 3), 1, 1, 1, 1, 1],
    [1, (3, 8)],
    [2, (2, 8)],
    [1, 1, 1, (1, 8)],
    [2, 2, 8],
]

REPLACE[8]['options'] = [
    [(4, 3), 1],
    [(4, 2), 2],
    [(4, 2), 1, 1],
    [(4, 1), 1, 1, 1],
    [4, 1, 1, 1, 1],
    [4, 2, 2],
    [1, (3, 4)],
    [2, (2, 4)],
    [1, 1, (2, 4)],
    [1, 1, 1, (1, 4)],
    [1, 1, 1, 1, 4],
    [2, 2, 4],
]

REPLACE[(16, 16)]['options'] = [
    [(16, 12, 3), 1],
    [(16, 12, 2), 2],
    [(16, 12, 2), 1, 1],
    [(16, 12, 1), 1, 1, 1],
    [(16, 12), 1, 1, 1, 1],
    [(16, 12), 2, 2],
    [(16, 8, 3), 1, 1, 1, 1, 1],
    [1, (3, 12, 16)],
    [2, (2, 12, 16)],
    [1, 1, (2, 12, 16)],
    [1, 1, 1, (1, 12, 16)],
    [2, 2, (12, 16)],
    [1, 1, 1, 1, (12, 16)],

]

# REPLACE[(12, 16)]['options'] = [

# ]

# REPLACE[(8, 16)]['options'] = [

# ]

# REPLACE[(16, 8)]['options'] = [

# ]

# REPLACE[(16, 4)]['options'] = [

# ]

# REPLACE[(4, 16)]['options'] = [

# ]

# REPLACE[(8, 12)]['options'] = [

# ]

# REPLACE[(12, 8)]['options'] = [

# ]

# REPLACE[(12, 4)]['options'] = [

# ]

# REPLACE[(8, 8)]['options'] = [

# ]

# REPLACE[(4, 8)]['options'] = [

# ]

# REPLACE[(8, 4)]['options'] = [

# ]

# REPLACE[(4, 4)]['options'] = [

# ]


for k in REPLACE:
    REPLACE[k]['weights'] = exp_weights(len(REPLACE[k]['options']), exponent=1.8)


# Check
for k in REPLACE:
    expected = k
    if isinstance(k, tuple):
        expected = sum(k)

    for option in REPLACE[k]['options']:
        total = 0
        for duration in option:
            if isinstance(duration, tuple):
                duration = sum(duration)
            total += duration

        if not expected == total:
            print k, option


"""
REPLACE[16]['options'] = [[12, 4], [(12, 2), 2], [8, 8], [8, 6, 2], [6, 2, 8], [6, 2, 6, 2], [6, 6, 4], [4, 6, 6], [6, (2, 6), 2]]

REPLACE[(16, 8)]['options'] = [[12, (4, 8)], [(16, 4), 4], [(16, 6), 2], [4, (12, 8)], [8, (8, 4), 4], [8, (8, 6), 2], [8, (8, 2), 6], [(16, 2), 6]]

REPLACE[(8, 16)]['options'] = [[(8, 12), 4], [(8, 8), 8], [(8, 8, 6), 2], [4, (4, 16)], [4, (4, 12), 4]]

REPLACE[(8, 8)]['options'] = [[(8, 4), 4], [(8, 6), 2], [4, (4, 8)], [4, (4, 4), 4]]

REPLACE[8]['options'] = [[4, 4], [6, 2], [2, 6], [2, (2, 2), 2]]
"""

def replace_note(duration):
    if duration in REPLACE:
        return weighted_choice(REPLACE[duration]['options'], REPLACE[duration]['weights'] )
    else:
        return [duration]
