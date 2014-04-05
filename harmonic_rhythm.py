# -*- coding: utf-8 -*-

import random

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
        [(16, 8), (8, 8), 8, 8, 8],

    ],
    8: [
        [16, 12, (4, 16), 16, 8, (8, 16), 16, 8, 8],

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
    """
    Given a section which is a list of configs for bars, return a list of Measures containing Chords with correct rhythms but no pitches set.

    """
    n_bars = len(section)
    raw = weighted_choice(OPTIONS[n_bars], WEIGHTS[n_bars])
    rhythm = parse_rhythm(raw)
    return raw, rhythm


def add_notes(rhythm, harmonies, unused):
    """Take a raw harmonic rhythm and add more notes by getting rid of ties and potentially subdividing exisisting notes."""
    new_rhythm = []
    new_harmonies = []
    new_unused = []
    for duration, harmony, unused_harmony in zip(rhythm, harmonies, unused):
        if isinstance(duration, tuple) and random.random() > 0.3:
            for dur in duration:
                new_rhythm.append(dur)
                new_harmonies.append(harmony)
                new_unused.append(unused_harmony)
        else:
            new_rhythm.append(duration)
            new_harmonies.append(harmony)
            new_unused.append(unused_harmony)

    return new_rhythm, new_harmonies, new_unused