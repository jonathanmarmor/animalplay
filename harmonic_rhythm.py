# -*- coding: utf-8 -*-

from utils import weighted_choice
from abjad_utils import parse_rhythm


# Durations in terms of 16th notes
OPTIONS = {
    1: [
        [16],
        [8, 8],
        [12, 4],
        [8, 4, 4],
        [4, 4, 8],
        [4, 12],
        [4, 8, 4],

    ],
    2: [
        [(16, 4), 12],

    ],
    4: [
        [(16, 8), (8, 16), 8, 8],

    ],
    8: [
        [16, 12, (4, 16), 16, 8, (8, 16), 16, 16],

    ],
    16: [
        [16, 16, 16, (16,
        16), (16, 16), (16,
        16), 16, 16, (16,
        16), 16, 16, 16]
    ]
}

WEIGHTS = {
    1: [
        40,
        100,
        100,
        45,
        15,
        12,
        4,
    ],
    2: [1],
    4: [1],
    8: [1],
    16: [1]
}


def choose(section):
# def choose(section):
    """
    Given a section which is a list of configs for bars, return a list of Measures containing Chords with correct rhythms but no pitches set.

    """

    n_bars = len(section)
    raw = weighted_choice(OPTIONS[n_bars], WEIGHTS[n_bars])
    rhythm = parse_rhythm(raw)
    return raw, rhythm





    # rv = []
    # for bar_config in section:
    #     durations = weighted_choice(OPTIONS[1], WEIGHTS[1])
    #     bar_config['harmonic_rhythm'] = durations

    #     bar = parse_rhythm(durations)[0]

    #     # chords = [Chord([], Duration(dur, 16)) for dur in durations]
    #     # bar = Measure(TimeSignature((4, 4)), chords)

    #     rv.append(bar)

    # return rv
