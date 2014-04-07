import random
from itertools import groupby
from collections import defaultdict

from utils import weighted_choice, exp_weights
from ornaments import replace_note


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


ORNAMENT_RATES = defaultdict(dict)
ORNAMENT_RATES[0]['Violin'] = 0.4
ORNAMENT_RATES[1]['Violin'] = 0.7
ORNAMENT_RATES[1]['Bb Clarinet'] = 0.9
ORNAMENT_RATES[2]['Bb Clarinet'] = 0.9
ORNAMENT_RATES[2]['Cello'] = 0.3
ORNAMENT_RATES[3]['Cello'] = 0.3
ORNAMENT_RATES[3]['Violin'] = 0.7


def add_notes(rhythm, harmonies, unused, soloist_name, movement_number):
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
        if random.random() < ORNAMENT_RATES[movement_number][soloist_name]:
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


def join_some_notes(rhythm, pitches):
    both = zip(rhythm, pitches)
    new_rhythm = []
    new_pitches = []
    for pitch, group in groupby(both, key=lambda x: x[1]):
        group = list(group)
        if len(group) == 2 and pitch != 'r' and random.random() < 0.5:
            new_r = []
            for r, p in group:
                if isinstance(r, tuple):
                    for rr in r:
                        new_r.append(rr)
                else:
                    new_r.append(r)
            new_rhythm.append(tuple(new_r))
            new_pitches.append(pitch)
        else:
            for r, p in group:
                new_rhythm.append(r)
                new_pitches.append(p)
    return new_rhythm, new_pitches


if __name__ == '__main__':
    import doctest
    doctest.testmod()
