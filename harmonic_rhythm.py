# -*- coding: utf-8 -*-

from utils import weighted_choice
from abjad_utils import get_rest_bar




options = [
    '1',
    '2 2',
    '2. 4',
    '2 4 4',
]

weights = [
    1,
    1,
    1,
    1,
]


def choose(phrase):
    return [get_rest_bar() for bar_config in phrase]



    # return weighted_choice(options, weights)


# def parse_rhythm_string(string):
#     pass



# one_bar = [
#     Measure(TimeSignature((4, 4)), [


#     ])


# ]
