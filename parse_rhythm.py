from abjad import attach
from abjad import Measure, TimeSignature, Rest, Chord, Duration
from abjad.tools.spannertools import Tie


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
    for i, duration in enumerate(rhythm):
        p = pitches[i]
        if total % denominator == 0:
            if not (len(measures) and len(measures[-1]) == 0):
                measure = Measure(TimeSignature((4, 4)), [])
                measures.append(measure)
        if isinstance(duration, tuple):
            tie = []
            to_tie.append(tie)
            for tuple_i, d in enumerate(duration):
                note = _make_note(p, d, denominator)
                measure.append(note)
                tie.append(note)
                total += d
                if total % denominator == 0 and not (tuple_i == len(duration) - 1 and i == len(rhythm) - 1):
                    measure = Measure(TimeSignature((4, 4)), [])
                    measures.append(measure)
        else:
            total += duration
            note = _make_note(p, duration, denominator)
            measure.append(note)
    for tie in to_tie:
        attach(Tie(), tie)
    return measures


one = [
    [8, 8],
    [12, 4],
    [16],
    [8, 4, 4],
    [4, 12],
    [4, 4, 8],
    [4, 8, 4],
    [4, 4, 4, 4],
]

two = [
    [12, (4, 8), 8],
    [8, (8, 4), 12],
    [(16, 8), 8],
    [8, (8, 12), 4],
    [(16, 12), 4],
    [(16, 8), 4, 4],
    [12, (4, 4), 12],
    [8, (8, 8), 8],
    [8, (8, 16)],
    [(16, 4), 12],
    [12, (4, 16)],
    [(16, 16)],
    [4, (12, 16)],
    [8, (8, 4), 8, 4],
    [(16, 4), 8, 4],
    [8, (8, 4), 4, 8],
    [(16, 4), 4, 8],
    [8, (8, 8), 4, 4],
    [4, (12, 8), 8],
    [4, 4, (8, 8), 8],
    [4, (12, 4), 12],
    [12, (4, 8), 4, 4],
    [4, 8, (4, 16)],
    [4, 4, (8, 4), 12],
    [4, 4, (8, 16)],
    [(16, 4), 4, 4, 4],
    [4, (12, 12), 4],
    [4, (12, 8), 4, 4],
    [4, 4, (8, 12), 4],
    [4, 4, 4, (4, 16)],
    [4, (12, 4), 8, 4],
    [4, (12, 4), 4, 8],
    [4, 4, 4, (4, 4), 12],
    [12, (4, 4), 4, 4, 4],
    [4, 8, (4, 4), 4, 8],
    [4, 8, (4, 4), 8, 4],
    [8, 4, (4, 4), 4, 8],
    [8, 4, (4, 4), 8, 4],
    [8, (8, 4), 4, 4, 4],
    [4, 4, (8, 4), 8, 4],
    [4, 4, (8, 4), 4, 8],
    [4, (12, 4), 4, 4, 4],
    [4, 4, (8, 4), 4, 4, 4],
    [4, 4, 4, (4, 8), 4, 4],
    [4, 4, 4, (4, 4), 4, 8],
    [4, 4, 4, (4, 4), 8, 4],
    [4, 8, (4, 4), 4, 4, 4],
    [8, 4, (4, 4), 4, 4, 4],
    [4, 4, 4, (4, 4), 4, 4, 4],
]

def test_parse_rhythm():
    print '='*40
    print 'one'
    print '='*40
    for r in one:
        print
        print r
        print parse_rhythm(r)
    print
    print '='*40
    print 'two'
    print '='*40
    for r in two:
        print
        print r
        print parse_rhythm(r)


if __name__ == '__main__':
    test_parse_rhythm()