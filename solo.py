import random
from itertools import groupby

from utils import weighted_choice, exp_weights


def get_actions(soloists):
    """
    >>> soloists = [\
        'Violin', 'Violin', 'Violin', 'Violin',\
        'Violin', 'Violin', None, 'Violin',\
        'Violin', 'Violin', 'Violin', 'Violin',\
        'Violin', 'Violin', None, None,\
        'Bb Clarinet', 'Bb Clarinet', 'Bb Clarinet', 'Bb Clarinet',\
        'Bb Clarinet', 'Bb Clarinet', 'Bb Clarinet', 'Cello',\
        'Cello', 'Cello', 'Cello', 'Cello',\
        'Cello', 'Cello', None, 'Violin'\
    ]
    >>> expected = [ \
        'play', 'play', 'play', 'play',\
        'play', 'exit', 'rest', 'enter',\
        'play', 'play', 'play', 'play',\
        'play', 'exit', 'rest', 'rest',\
        'enter', 'play', 'play', 'play',\
        'play', 'play', 'exit', 'enter',\
        'play', 'play', 'play', 'play',\
        'play', 'exit', 'rest', 'enter'\
    ]
    >>> actions = get_actions(soloists)
    >>> assert actions == expected

    """

    actions = []
    first = True
    for soloist, sections in groupby(soloists):
        if soloist:
            section_actions = []
            for s in sections:
                section_actions.append('play')
            if len(section_actions) > 0 and not first:
                section_actions[0] = 'enter'
            if len(section_actions) > 1:
                section_actions[-1] = 'exit'
            actions.extend(section_actions)
        else:
            for section in sections:
                actions.append('rest')
        first = False
    return actions


def rank_by_distance(previous, options):
    distance_preferences = [1, 2, 3, 4, 5, 0, 7, 6]
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
        'Violin': {'lowest': 0, 'highest': 22},
    },
    1: {
        'Violin': {'lowest': 7, 'highest': 28},
        'Bb Clarinet': {'lowest': -5, 'highest': 25},
    },
    2: {
        'Bb Clarinet': {'lowest': -5, 'highest': 25},
        'Cello': {'lowest': -24, 'highest': 2},
    },
    3: {
        'Violin': {'lowest': -5, 'highest': 24},
        'Cello': {'lowest': -24, 'highest': 2},
    },
}

OUT_OF_TUNE_RATE = \
    [random.uniform(0.0, 0.6) for _ in range(8)] + \
    [random.uniform(0.0, 0.2) for _ in range(8)] + \
    [random.uniform(0.0, 0.1) for _ in range(8)] + \
    [random.uniform(0.0, 0.2) for _ in range(8)]

FIRST_NOTE = True

def next_soloist_note(soloist_name, previous, harmony, movement_number, volume_section_number):
    out_of_tune_rate = OUT_OF_TUNE_RATE[volume_section_number]
    global FIRST_NOTE
    if FIRST_NOTE:
        out_of_tune_rate = 1.0
        FIRST_NOTE = False

    if soloist_name == 'Bb Clarinet':
        out_of_tune_rate = 0.0

    registers = REGISTERS[movement_number]
    register = registers[soloist_name]
    lowest = register['lowest']
    highest = register['highest']
    if previous == None:
        previous = random.randint(lowest, highest)

    if random.random() < out_of_tune_rate:
        options = [p for p in range(previous - 2, previous + 3) if p >= lowest and p <= highest]
        p = random.choice(options)
        interval = random.choice([1, 2])
        if interval == 2:
            pitch = [p - 1, p + 1]
        elif interval == 1:
            up_or_down = random.choice([1, -1])
            pitch = [p, p + up_or_down]
            pitch.sort()
    else:
        options = [p for p in range(previous - 7, previous + 8) if p % 12 in harmony and p >= lowest and p <= highest]
        ranked_by_distance = rank_by_distance(previous, options)
        weights = exp_weights(len(ranked_by_distance), exponent=1.5)
        pitch = weighted_choice(ranked_by_distance, weights)

    return pitch


def replace_note(duration):
    if duration == 16:
        options = [[12, 4], [(12, 2), 2], [8, 8], [8, 6, 2], [6, 2, 8], [6, 2, 6, 2], [6, 6, 4], [4, 6, 6], [6, (2, 6), 2]]
        weights = range(len(options), 0, -1)
        return weighted_choice(options, weights)

    elif duration == (16, 8):
        options = [[12, (4, 8)], [(16, 4), 4], [(16, 6), 2], [4, (12, 8)], [8, (8, 4), 4], [8, (8, 6), 2], [8, (8, 2), 6], [(16, 2), 6]]
        weights = range(len(options), 0, -1)
        return weighted_choice(options, weights)

    elif duration == (8, 16):
        options = [[(8, 12), 4], [(8, 8), 8], [(8, 8, 6), 2], [4, (4, 16)], [4, (4, 12), 4]]
        weights = range(len(options), 0, -1)
        return weighted_choice(options, weights)

    elif duration == (8, 8):
        options = [[(8, 4), 4], [(8, 6), 2], [4, (4, 8)], [4, (4, 4), 4]]
        weights = range(len(options), 0, -1)
        return weighted_choice(options, weights)

    elif duration == 8:
        options = [[4, 4], [6, 2], [2, 6], [2, (2, 2), 2]]
        weights = exp_weights(len(options), exponent=1.8)
        return weighted_choice(options, weights)

    else:
        return [duration]


def add_notes(rhythm, harmonies, unused):
    """Take a raw harmonic rhythm and add more notes by getting rid of ties and potentially subdividing exisisting notes."""
    new_rhythm = []
    new_harmonies = []
    new_unused = []
    for duration, harmony, unused_harmony in zip(rhythm, harmonies, unused):
        if isinstance(duration, tuple) and random.random() > 0.5:
            for dur in duration:
                new_rhythm.append(dur)
                new_harmonies.append(harmony)
                new_unused.append(unused_harmony)
        else:
            new_rhythm.append(duration)
            new_harmonies.append(harmony)
            new_unused.append(unused_harmony)

    newer_rhythm = []
    newer_harmonies = []
    newer_unused = []
    for duration, harmony, unused_harmony in zip(new_rhythm, new_harmonies, new_unused):
        if random.random() > 0.85:
            durations = replace_note(duration)
            for duration in durations:
                newer_rhythm.append(duration)
                newer_harmonies.append(harmony)
                newer_unused.append(unused_harmony)
        else:
            newer_rhythm.append(duration)
            newer_harmonies.append(harmony)
            newer_unused.append(unused_harmony)

    return newer_rhythm, newer_harmonies, newer_unused


if __name__ == '__main__':
    import doctest
    doctest.testmod()
