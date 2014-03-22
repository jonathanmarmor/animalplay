from abjad import attach
from abjad import (Measure, TimeSignature, Rest, Chord, Duration, Container)
from abjad.tools.spannertools import Tie, Beam


def get_rest_bar(numerator=4, denominator=4):
    return Measure(TimeSignature((numerator, denominator)), [Rest(Duration(1, 1))])


def get_empty_bar(numerator=4, denominator=4):
    return Measure(TimeSignature((numerator, denominator)), [])


def get_one_note_bar(pitch):
    return Measure(TimeSignature((4, 4)), [get_note(pitch, (1, 1))])


# TODO finish implementing this.
def get_harmonic_rhythm_bar(harmonic_rhythm):
    return Measure(TimeSignature((4, 4)), [
        get_note([]),
    ])


def get_note(notes, duration):
    if isinstance(notes, int):
        notes = [notes]
    return Chord(notes, Duration(*(duration)))


def tie(notes):
    attach(Tie(), notes)


def beam(notes):
    attach(Beam(), notes)


def container(items, is_simultaneous=False):
    c = Container()
    c.is_simultaneous = is_simultaneous
    if not isinstance(items, list):
        items = [items]
    c.extend(items)
    return c