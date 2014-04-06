import random
from itertools import groupby

from utils import get_interval_class, exp_weights, weighted_choice


def rank_by_distance(previous, options):
    distance_preferences = [2, 1, 0, 3, 4, 5, 7, 6]
    distances = [abs(previous - p) for p in options]
    ranked = sorted(zip(distances, options), key=lambda x: distance_preferences.index(x[0]))

    # Shuffle rank of pitches that have the same distance
    distance_groups = groupby(ranked, key=lambda x: x[0])
    new_ranks = []
    for distance, group in distance_groups:
        group = list(group)
        random.shuffle(group)
        new_ranks.extend(group)

    return [item[1] for item in new_ranks]


REGISTERS = {
    0: {
        'Bb Clarinet': {'lowest': -10, 'highest': 10},
        'Cello': {'lowest': -10, 'highest': 10},
    },
    1: {
        'Violin': {'lowest': -5, 'highest': 15},
        'Bb Clarinet': {'lowest': -10, 'highest': 10},
        'Cello': {'lowest': -10, 'highest': 10},
    },
    2: {
        'Violin': {'lowest': -5, 'highest': 15},
        'Bb Clarinet': {'lowest': -10, 'highest': 10},
        'Cello': {'lowest': -10, 'highest': 10},
    },
    3: {
        'Violin': {'lowest': 0, 'highest': 24},
        'Bb Clarinet': {'lowest': 0, 'highest': 24},
        'Cello': {'lowest': -10, 'highest': 10},
    },
}


def get_options(previous, harmony, lowest, highest):
    return [p for p in range(previous - 7, previous + 8) if p % 12 in harmony and p >= lowest and p <= highest]


def build_options(previous, harmony, unused_harmony, lowest, highest):
    unused_options = get_options(previous, unused_harmony, lowest, highest)
    unused_ranked = rank_by_distance(previous, unused_options)

    used = list(set(harmony) - set(unused_harmony))
    used_options = get_options(previous, used, lowest, highest)
    used_ranked = rank_by_distance(previous, used_options)
    options = unused_ranked + used_ranked

    return options


def next_accompaniment_notes(name_a, name_b, previous_a, previous_b, harmony, unused_harmony, movement_number):
    registers = REGISTERS[movement_number]

    a_register = registers[name_a]
    b_register = registers[name_b]

    if previous_a == None:
        previous_a = random.randint(a_register['lowest'], a_register['highest'])

    if previous_b == None:
        previous_b = random.randint(b_register['lowest'], b_register['highest'])

    a_options = build_options(previous_a, harmony, unused_harmony, a_register['lowest'], registers[name_a]['highest'])
    b_options = build_options(previous_b, harmony, unused_harmony, b_register['lowest'], registers[name_b]['highest'])

    a_weights = exp_weights(len(a_options))
    b_weights = exp_weights(len(b_options))

    max_weight = a_weights[0] + b_weights[0]

    weighted_interval_options = []
    for a, a_weight in zip(a_options, a_weights):
        for b, b_weight in zip(b_options, b_weights):
            interval_class = get_interval_class(a, b)
            if interval_class == 1:
                continue
            if interval_class in [5, 4, 3]:
                weight = max_weight
            elif interval_class in [2, 0]:
                weight = max_weight / 2
            elif interval_class == 6:
                weight = 0

            if a == b:
                weight = 0

            weight = weight + a_weight + b_weight

            weighted_interval_options.append(((a, b), weight))

    return weighted_choice(*zip(*weighted_interval_options))


def add_accompaniment_notes(rhythm, harmonies, unused):
    """Take a raw harmonic rhythm and add more notes by getting rid of ties and potentially subdividing exisisting notes."""
    new_rhythm = []
    new_harmonies = []
    new_unused = []
    for duration, harmony, unused_harmony in zip(rhythm, harmonies, unused):
        if isinstance(duration, tuple) and random.random() > 0.7:
            for dur in duration:
                new_rhythm.append(dur)
                new_harmonies.append(harmony)
                new_unused.append(unused_harmony)
        else:
            new_rhythm.append(duration)
            new_harmonies.append(harmony)
            new_unused.append(unused_harmony)

    return new_rhythm, new_harmonies, new_unused
