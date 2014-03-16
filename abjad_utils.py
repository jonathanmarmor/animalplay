from abjad import attach
from abjad import (Measure, TimeSignature, Rest, Chord, Duration, Container)
from abjad.tools.spannertools import Tie


def get_empty_bar():
    return Measure(TimeSignature((4, 4)), [Rest(Duration(1, 1))])


def get_note(notes, duration):
    if isinstance(notes, int):
        notes = [notes]
    return Chord(notes, Duration(*(duration)))


def tie(notes):
    attach(Tie(), notes)


def container(items, is_simultaneous=False):
    c = Container()
    c.is_simultaneous = is_simultaneous
    if not isinstance(items, list):
        items = [items]
    c.extend(items)
    return c