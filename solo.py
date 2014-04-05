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
    distance_preferences = [2, 1, 3, 4, 0, 5, 7, 6]
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


# def get_options(previous, harmony, lowest, highest):
#     return [p for p in range(previous - 7, previous + 8) if p % 12 in harmony and p >= lowest and p <= highest]


# def build_options(previous, harmony, unused_harmony, lowest, highest):
#     unused_options = get_options(previous, unused_harmony, lowest, highest)
#     unused_ranked = rank_by_distance(previous, unused_options)

#     used = list(set(harmony) - set(unused_harmony))
#     used_options = get_options(previous, used, lowest, highest)
#     used_ranked = rank_by_distance(previous, used_options)
#     options = unused_ranked + used_ranked

#     return options




def next_soloist_note(soloist_name, previous, harmony, movement_number):
    registers = REGISTERS[movement_number]
    register = registers[soloist_name]
    lowest = register['lowest']
    highest = register['highest']
    if previous == None:
        previous = random.randint(lowest, highest)

    options = [p for p in range(previous - 7, previous + 8) if p % 12 in harmony and p >= lowest and p <= highest]
    ranked_by_distance = rank_by_distance(previous, options)

    weights = exp_weights(len(ranked_by_distance))

    return weighted_choice(ranked_by_distance, weights)






if __name__ == '__main__':
    import doctest
    doctest.testmod()
