from abjad import attach
from abjad import (Measure, TimeSignature, Rest, Chord, Duration, Container)
from abjad.tools.spannertools import Tie, Beam

# from abjad.tools.markuptools import Markup
# from abjad.tools.spannertools import TextScriptSpanner
from abjad.tools.indicatortools import LilyPondCommand
from abjad.tools.indicatortools import Dynamic
from abjad.tools.indicatortools import BarLine


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
        if isinstance(p, int):
            p = [p]
        chord = Chord(p, Duration(dur, 16))
        chords.append(chord)
    return Measure(TimeSignature((4, 4)), chords)



# def get_harmonic_rhythm_bar(harmonic_rhythm, rhythm_string):


#     notes = [Chord([], Duration(1, 1))]

#     return Measure(TimeSignature((4, 4)), notes)



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