import itertools
from collections import Counter

import utils


def partitions(n):
    """Get all the partitions of an integer n.

    From: http://homepages.ed.ac.uk/jkellehe/partitions.php

    >>> [part for part in partitions(4)]
    [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]

    """
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def inversions(chord):
    """Get all inversions of a list of intervals.

    >>> [inv for inv in inversions((4, 3, 5))]
    [(4, 3, 5), (3, 5, 4), (5, 4, 3)]

    NOTE: for interval lists, not pitch classes.
    """
    chord = list(chord)
    for i, note in enumerate(chord):
        inverted = chord[i:] + chord[:i]
        yield tuple(inverted)


def get_chord_classes(max_notes=6):
    """Get all

    """
    chord_classes = set()
    for partition in partitions(12):
        len_partition = len(partition)
        if len_partition > 1 and len_partition <= max_notes:
            for perm in itertools.permutations(partition):
                # If no inversions of perm are in chord_classes, add perm
                if not any([inversion in chord_classes for inversion in inversions(perm)]):
                    chord_classes.add(perm)
    return chord_classes


def get_interval_content(chord):
    """Get counts of each interval appearing in a chord
    (m2, M2, m3, M3, P4, TT)

    >>> get_interval_content((4, 3, 5))
    (0, 0, 2, 2, 2, 0)

    >>> get_interval_content((4, 3, 3, 2))
    (0, 2, 4, 2, 2, 2)

    """
    chord = list(chord)
    content = Counter()
    n_intervals = len(chord)
    for width in range(1, n_intervals):
        for i, n in enumerate(chord):
            if i + width < n_intervals:
                notes = chord[i:i + width]
            else:
                notes = chord[i:] + chord[:(i + width) % n_intervals]
            interval = sum(notes)
            if interval < 6:
                content[interval] += 1
    return tuple([content[i] for i in range(1, 7)])


def score_chord(chord):
    intervals = get_interval_content(chord)
    # From http://musiccog.ohio-state.edu/home/data/_uploaded/pdf/Music%20Perception/MP%2094Sp%20Interval-Class%20Content%20in%20Equally%20Tempered%20Pitch-Class%20Sets%20-%20Common%20Scales%20Exhibit%20optimum%20Tonal%20Consonance.pdf
    # weights = (-1.428, -0.582, 0.594, 0.386, 1.240, -0.453)
    # My tweaks
    weights = (-1.628, 0.052, 0.971, 1.086, 1.84, -0.997)
    n_notes = len(chord)
    score = sum([count * weight for count, weight in zip(intervals, weights)]) / n_notes
    # collapse rankings by number of notes a bit
    n_notes_correction = utils.scale(6 - n_notes, -5, 5, -2.75, 2.75)
    return score + n_notes_correction


def rank_chords():
    ranked = []
    for chord in get_chord_classes():
        score = score_chord(chord)
        ranked.append((chord, score))
    return sorted(ranked, key=lambda x: x[1], reverse=True)
