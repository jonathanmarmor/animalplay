from abjad import attach
from abjad import (Measure, TimeSignature, Rest, Chord, Duration, Container)
from abjad.tools.spannertools import Tie, Beam, Crescendo, Decrescendo

# from abjad.tools.markuptools import Markup
# from abjad.tools.spannertools import TextScriptSpanner
from abjad.tools.indicatortools import LilyPondCommand
from abjad.tools.indicatortools import Dynamic
from abjad.tools.indicatortools import BarLine


def is_rest(note):
    return isinstance(note, Rest)

def get_rest_bar(numerator=4, denominator=4):
    return Measure(TimeSignature((numerator, denominator)), [Rest(Duration(1, 1))])


def get_empty_bar(numerator=4, denominator=4):
    return Measure(TimeSignature((numerator, denominator)), [])


def get_one_note_bar(pitch):
    return Measure(TimeSignature((4, 4)), [get_note(pitch, (1, 1))])


def get_bar(durations, pitches=None):
    if not pitches:
        pitches = [[] for _ in durations]
    chords = []
    for dur, p in zip(durations, pitches):
        if p == 'r':
            chord = Rest(Duration(dur, 16))
        else:
            if isinstance(p, int):
                p = [p]
            chord = Chord(p, Duration(dur, 16))
        chords.append(chord)
    return Measure(TimeSignature((4, 4)), chords)


def _make_note(pitches, duration, denominator):
    if pitches == 'r':
        return Rest(Duration(duration, denominator))
    if isinstance(pitches, int):
        pitches = [pitches]
    return Chord(pitches, Duration(duration, denominator))


def parse_rhythm(rhythm, pitches=None, denominator=16):
    """Turn a list of 16th note durations with tied notes in tuples into a list of abjad Measures.

    >>> x = parse_rhythm([(16, 4), 12])
    >>> x
    [Measure((4, 4), "<f'>1"), Measure((4, 4), "<f'>4 <f'>2.")]
    >>> from abjad import Staff, format
    >>> s = Staff(x)
    >>> [l.note_heads.append(4) for l in s.select_leaves()]
    [None, None, None]
    >>> print(format(s))
    \\new Staff {
        {
            \\time 4/4
            <e'>1 ~
        }
        {
            <e'>4
            <e'>2.
        }
    }

    """
    if not pitches:
        pitches = [[] for _ in rhythm]
    if len(rhythm) != len(pitches):
        raise Exception('Length of rhythm and pitches doesnt match.')
    measures = []
    total = 0
    to_tie = []
    for duration, p in zip(rhythm, pitches):
        if total % denominator == 0:
            if not (len(measures) and len(measures[-1]) == 0):
                measure = Measure(TimeSignature((4, 4)), [])
                measures.append(measure)
        if isinstance(duration, tuple):
            tie = []
            to_tie.append(tie)
            for d in duration:
                note = _make_note(p, d, denominator)
                measure.append(note)
                tie.append(note)
                total += d
                if total % denominator == 0:
                    measure = Measure(TimeSignature((4, 4)), [])
                    measures.append(measure)
        else:
            total += duration
            note = _make_note(p, duration, denominator)
            measure.append(note)
    for tie in to_tie:
        attach(Tie(), tie)
    return measures


def get_note(notes, duration):
    if isinstance(notes, int):
        notes = [notes]
    return Chord(notes, Duration(*(duration)))


def tie(notes):
    attach(Tie(), notes)


def beam(notes):
    attach(Beam(), notes)


def crescendo(notes, decrescendo=False):
    f = Crescendo
    if decrescendo:
        f = Decrescendo
    attach(f(include_rests=True), notes)


def container(items, is_simultaneous=False):
    c = Container()
    c.is_simultaneous = is_simultaneous
    if not isinstance(items, list):
        items = [items]
    c.extend(items)
    return c


def add_rehearsal_mark(measure):
    command = LilyPondCommand(r'mark \default', 'before')
    attach(command, measure)


def add_dynamic(item, dynamic):
    attach(Dynamic(dynamic), item)


def add_final_barline(staff):
    attach(BarLine('|.'), staff[-1][-1])


def add_double_barline(item):
    attach(BarLine('||'), item)


def lookup_duration(quarterlengths):
    d = {
        4.0: '1',
        3.0: '2.',
        2.0: '2',
        1.5: '4.',
        1.0: '4',
        0.75: '8.',
        0.5: '8',
        0.25: '16',
    }
    return d[quarterlengths]


# def triplet(notes):
#     return Tuplet(Multiplier(2, 3), notes)



"""

notes = [
    Note(2, Duration(1, 16)),
    Note(4, Duration(1, 16)),
    Note(5, Duration(1, 8)),
    Note(5, Duration(1, 8)),
    Tuplet(Multiplier(2, 3), [
        Note(4, Duration(1, 16)),
        Note(5, Duration(1, 16)),
        Note(4, Duration(1, 16)),
    ]),
    Note(3, Duration(1, 8)),
    Note(0, Duration(1, 8)),
    Note(0, Duration(1, 8)),
    Note(7, Duration(1, 8)),
]

[.25, .25, .5, .5, (.25, .25, .25), ]


s = Staff(Measure(

[r"{}16 {}16 {}8 {}8 \times 2/3 {{ {}16 {}16 {}16~ }} {}8 {}8 {}8 {}8", r"{}8 {}8 {}8 {}8~ {}2"]

'2 2 4 4 tup( 2 2 tie( 2 tup) 4 tie) 4 4 4 4 4 4 tie( 4 16 tie)'



'1 1 2 2 tup( 1 1 tie( 1 tup) 2 tie) 2 2 2 2 2 2 tie( 2 8 tie)'



'<>16 <>16 <>8 <>8 \\times 2/3 { <>16 <>16 <>16~ } <>8 <>16. <>32~ <>8 <>8~ | <>4. <>8~ <>2'

"""


# def parse_bar_string(bar_string):
#     measure = Measure(TimeSignature((4, 4)), [])

#     parts = bar_string.split(' ')
#     in_tuplet = False
#     for part in parts:
#         print part,
#         if part == 't(':
#             tuplet = []
#             in_tuplet = True
#             continue
#         if part == ')':
#             in_tuplet = False
#             tuplet_string = ' '.join(tuplet)
#             tuplet_string = '\\times 2/3 {{ {} }} '.format(tuplet_string)

#             measure.append(tuplet_string)
#             continue

#         note = '<>{} '.format(part)

#         if in_tuplet:
#             tuplet.append(note)
#         else:
#             measure.append(note)

#     return measure


# def compile_rhythm(bars):
#     """
#     ['16 16 8 8 t( 16 16 16~ ) 8 8 8 8', '8 8 8 8~ 2']

#     """
#     if isinstance(bars, basestring):
#         bars = [bars]
#     return [parse_bar_string(string) for string in bars]


# '<>16 <>16 <>8 <>8 \\times 2/3 { 16 16 16~ }' '8 8 8 8', '8 8 8 8~ 2']





# '\times 2/3 { <>8 <>8 <>8 }'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
