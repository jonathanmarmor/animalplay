# -*- coding: utf-8 -*-

import random
import itertools
from collections import defaultdict

from harmony import ranked_roots
from utils import weighted_choice, exp_weights


def rank_by_distance(previous, options):
    distance_preferences = [2, 1, 0, 3, 4, 5, 7, 6]
    distances = [abs(previous - p) for p in options]
    ranked = sorted(zip(distances, options), key=lambda x: distance_preferences.index(x[0]))

    # Shuffle rank of pitches that have the same distance
    distance_groups = itertools.groupby(ranked, key=lambda x: x[0])
    new_ranks = []
    for distance, group in distance_groups:
        group = list(group)
        random.shuffle(group)
        new_ranks.extend(group)

    return [item[1] for item in new_ranks]


def rank_by_best_root(harmony, options):
    ranked = []
    roots = ranked_roots(harmony)
    for root in roots:
        pitches = [p for p in options if p % 12 == root]
        random.shuffle(pitches)
        ranked.extend(pitches)
    return ranked


LEFT_LOWEST_PITCH = -24
LEFT_HIGHEST_PITCH = -1  # TODO this will change with the lowest pitch of the right hand at any given moment


def next_piano_bass_note(previous, harmony):
    options = [p for p in range(previous - 7, previous + 8) if p % 12 in harmony and p >= LEFT_LOWEST_PITCH and p <= LEFT_HIGHEST_PITCH]
    ranked_by_distance = rank_by_distance(previous, options)
    ranked_by_best_root = rank_by_best_root(harmony, options)

    ranks = defaultdict(list)
    len_options = len(options)
    for p in options:
        distance_rank = len_options - ranked_by_distance.index(p)
        root_rank = len_options - ranked_by_best_root.index(p)
        rank = distance_rank + root_rank
        ranks[rank].append(p)
    ranked = []
    for k in sorted(ranks.keys(), reverse=True):
        random.shuffle(ranks[k])
        ranked.extend(ranks[k])

    weights = exp_weights(len(ranked))
    return weighted_choice(ranked, weights)









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

