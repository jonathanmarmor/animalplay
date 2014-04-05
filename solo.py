import random
from itertools import groupby


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


def next_soloist_note(soloist_name, previous, harmony, unused_harmony):
    return random.choice(harmony)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
