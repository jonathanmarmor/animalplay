# -*- coding: utf-8 -*-

# these are notes from a melody fragment from "Secret Heart" by Ron Sexsmith
# 0 3 2 3 2 0 10 0 7

# 5 8 7 8 7 5 3 5 0

#

# [0.25, 0.25, (0.5, 0.5), 0.166, 0.166, 0.166, 0.5, 0.5, 0.5, 0.5]

# 0, 2, 3, 2, 3, 2, 1, 10, 10, 5


from abjad import Note, Pitch


rhtyhm_options = [
    (4,),
    (2, 2),
    (3, 1),
    (2, 1, 1),
    (1, 1, 2),
    (4.5, 0.5)
    (1.5, 1.5, 1),
    (1, 1.5, 1.5)
]


def choose(n_bars):
    return [random.choice(options) for _ in xrange(n_bars)]


def get_melody():
    melody = []



    return melody