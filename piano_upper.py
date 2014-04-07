from itertools import groupby
import random

from harmony import score_chord, pitches_to_intervals
from utils import weighted_choice, exp_weights


LOWEST = 0
HIGHEST = 24


def rank_by_distance(previous_center, options):
    distance_preferences = range(20)
    distances = [abs(previous_center - p) for p in options]
    ranked = sorted(zip(distances, options), key=lambda x: distance_preferences.index(x[0]))

    # Shuffle rank of pitches that have the same distance
    distance_groups = groupby(ranked, key=lambda x: x[0])
    new_ranks = []
    for distance, group in distance_groups:
        group = list(group)
        random.shuffle(group)
        new_ranks.extend(group)

    return [item[1] for item in new_ranks if item[1] != None]


# def transition(a, b):
#     distances = defaultdict(list)
#     for pitch_a in a:
#         for pitch_b in b:
#             distance = abs(pitch_a - pitch_b)
#             distances[pitch_a].append(distance)
#         distances[pitch_a].sort()
#     return distances


def rank_by_harmony_score(chord, options):
    items = []
    for p in options:
        if p % 12 in chord:
            items.append((p, 10))
        else:
            c = chord[:]
            c.append(p)
            c.sort()
            intervals = pitches_to_intervals(c)
            score = score_chord(intervals)
            item = (p, score)
            items.append(item)
    return [p for p, score in sorted(items, key=lambda x: x[1], reverse=True) if p not in chord]


def get_center(chord):
    total = sum(chord)
    n_notes = len(chord)
    n_notes = float(n_notes)
    avg = total / n_notes
    avg = round(avg)
    avg = int(avg)
    return avg


"""
- has to have at least one note
- has to use all the unused_harmony pitch classes
- all notes have to be within an octave (inclusive)
- shouldn't be a big jump from previous. Not sure how to define that.

"""

def next_piano_right_hand_chord(previous, harmony, unused_harmony):
    chord = []
    previous = [p for p in previous if p != None]

    previous_center = get_center(previous)

    for pc in unused_harmony:
        unused_options = [p for p in range(previous_center - 10, previous_center + 11) if p % 12 == pc and p >= LOWEST and p <= HIGHEST]
        ranked = rank_by_distance(previous_center, unused_options)
        chord.append(ranked[0])

    len_chord = len(chord)
    if len_chord < 5:
        n_notes = random.randint(len_chord, 5)

        if len_chord < n_notes:
            for _ in range(n_notes - len_chord):
                if chord:
                    lowest = max(chord) - 13
                    highest = min(chord) + 14
                else:
                    lowest = previous_center - 10
                    highest = previous_center + 11

                options = [p for p in range(lowest, highest) if p % 12 in harmony and p >= LOWEST and p <= HIGHEST and p not in chord]
                if chord:
                    print 'harm'
                    ranked = rank_by_harmony_score(chord, options)
                    if not ranked:
                        print 'distance 1'
                        ranked = rank_by_distance(previous_center, options)
                else:
                    print 'distance 2'
                    ranked = rank_by_distance(previous_center, options)
                if not ranked:
                    Exception('couldnt get any ranked notes. Figure out why.')

                choice = weighted_choice(ranked, exp_weights(len(ranked), exponent=4))

                # if choice == None:
                #     return next_piano_right_hand_chord(previous, harmony, unused_harmony)

                chord.append(choice)
    chord.sort()
    return chord
