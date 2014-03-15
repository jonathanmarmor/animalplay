# -*- coding: utf-8 -*-

from collections import Counter
import random

import harmony
from utils import try_f, AnimalPlayException


# transition_scores = [
#     1000,  # Unison
#     1000,  # m2
#     1000,  # M2
#     100,   # m3
#     10,    # M3
#     10,    # P4
#     1      # Tritone
# ]


# def get_transitions(a, b):
#     """
#     >>> get_transitions((0, 4, 7), (0, 3, 10))
#     {
#         0: {
#             0: 0,
#             3: 3,
#             10: 2
#         },
#         4: {
#             0: 4,
#             3: 1,
#             10: 6
#         },
#         7: {
#             0: 5,
#             3: 4,
#             10: 3
#         }
#     }
#     {0: {0: 0, 3: 3, 10: 2}, 4: {0: 4, 3: 1, 10: 6}, 7: {0: 5, 3: 4, 10: 3}}
#     {0: {0: 0, 3: 3, 10: 2}, 4: {0: 4, 3: 1, 10: 6}, 7: {0: 5, 3: 4, 10: 3}}

#     """
#     transitions = {}
#     for na in a:
#         transitions[na] = {}
#         for nb in b:
#             interval = (na - nb) % 12
#             if interval > 6:
#                 interval = 12 - interval
#             transitions[na][nb] = interval
#     return transitions


# def test():
#     n = 10
#     roots = [random.choice(range(12)) for _ in xrange(n)]
#     chord_types = [harmony.choose() for _ in xrange(n)]
#     chords = [sorted(harmony.intervals_to_pcs(r, c)) for r, c in zip(roots, chord_types)]

#     pairs = pairwise(chords)
#     for pair in pairs:
#         evaluate(pair)

#     return chords




def pick_chord():
    return sorted(harmony.intervals_to_pcs(random.choice(range(12)), harmony.choose()))


def choose_initial_chord(l_register, r_register):
    chord = {'l': [], 'r': []}
    register = {
        'l': l_register,
        'r': r_register
    }
    # a chordtype chosen based on weights on a random root
    harmony = pick_chord()
    hands = ['r', 'l']
    # make sure all pitches in the chord are used
    for pc in harmony:
        # TODO make sure there no more than 5 notes per hand
        # TODO prefer putting notes in the right hand
        # TODO only allow single notes and dyads a fifth or larger in the left hand
        for hand in hands:
            if len(register[hand]) == 5:
                hands.remove(hand)
        hand = random.choice(hands)
        opts = [p for p in register[hand] if (p % 12) == pc]
        p = random.choice(opts)
        chord[hand].append(p)




    # # make sure all pitches in the chord are used
    # depth = 0
    # opts = 'not set'
    # while covered:
    #     opts = {
    #         'l': [p for p in l_register if (p % 12) in covered],
    #         'r': [p for p in r_register if (p % 12) in covered]
    #     }
    #     hand = random.choice(['l', 'r'])
    #     if opts[hand] and len(chord[hand]) < 5:
    #         pitch = random.choice(opts[hand])
    #         opts[hand].remove(pitch)
    #         pitchclass = pitch % 12
    #         covered.remove(pitchclass)
    #         chord[hand].append(pitch)

    #     depth += 1
    #     if depth > 1000:
    #         raise AnimalPlayException('hung out in choose_initial_chord "while covered" loop for too long')

    hands = ['r', 'l']
    for hand in hands:
        if len(chord[hand]) >= 5:
            hands.remove(hand)

    # add octave doubling
    for hand in hands:
        opts = [p for p in register[hand] if (p % 12) in harmony and p not in chord[hand]]
        top = 5
        if len(opts) < 5:
            top = len(opts)
        n_extra_notes = random.randint(0, top)
        for _ in range(n_extra_notes):
            p = random.choice(opts)
            opts.remove(p)
            chord[hand].append(p)
        chord[hand].sort()

    return chord


def run():
    # all notes allowed. three octaves from one oct below middle c
    register = range(48, 85)
    # choose a pitch to use as an anchor so we can decide the anchors for each hand
    anchor = random.choice(register)
    # choose the distance above and below the anchor for each hands' range
    spread = random.randint(0, 7)
    # each hand within an octave
    l_highest = anchor - spread
    l_register = range(l_highest - 13, l_highest + 1)
    r_lowest = anchor + spread
    r_register = range(r_lowest, r_lowest + 14)

    out = {
        'r': [],
        'l': []
    }

    chord = try_f(choose_initial_chord, args=[l_register, r_register])
    # chord = choose_initial_chord(l_register, r_register)
    out['l'].append(chord['l'])
    out['r'].append(chord['r'])

    return out


def count_notes(out):
    c = Counter()
    for _ in xrange(1000):
        out = run()
        c[len(out['l'][0])] += 1
        c[len(out['r'][0])] += 1
    return c
