# -*- coding: utf-8 -*-

from abjad import Chord, Duration, Measure, TimeSignature

from utils import weighted_choice
# from abjad_utils import get_rest_bar


# Durations in terms of 16th notes
options = {
    1: [
        [16],
        [8, 8],
        [12, 4],
        [8, 4, 4],
        [4, 4, 8],
    ]
}

weights = {
    1: [
        3,
        4,
        4,
        2,
        1
    ]
}


def choose(section):
    """
    Given a section which is a list of configs for bars, return a list of Measures containing Chords with correct rhythms but no pitches set.

    """
    rv = []
    for bar_config in section:

        durations = weighted_choice(options[1], weights[1])
        bar_config['harmonic_rhythm'] = durations

        chords = [Chord([], Duration(dur, 16)) for dur in durations]

        bar = Measure(TimeSignature((4, 4)), chords)

        rv.append(bar)

    return rv


