# -*- coding: utf-8 -*-

from utils import weighted_choice


options = [
    (4,),
    (2, 2),
    (3, 1),
    (2, 1, 1),
]


weights = [
    1,
    1,
    1,
    1,
]


def choose(n_bars):
    return weighted_choice(options, weights)
