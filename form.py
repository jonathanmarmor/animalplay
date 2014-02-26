import random

from utils import weighted_choice, try_f, AnimalPlayException


soloist = {
    'I': 'violin',
    'II': 'violin',
    'III': 'clarinet',
    'IV': 'cello'
}
accompanists = {
    'I': ['clarinet', 'cello'],
    'II': ['clarinet', 'cello'],
    'III': ['violin', 'cello'],
    'IV': ['clarinet', 'violin']
}
n_bars_options = {
    'I': [8, 4],
    'II': [8, 4, 2],
    'III': [4, 8, 16, 2],
    'IV': [8, 2, 4],
}
n_bars_weights = {
    'I': [1, 1],
    'II': [8, 7, 1],
    'III': [14, 11, 6, 1],
    'IV': [3, 3, 2]
}

drone_options = range(12)

dynamics_a = {
    'drone': 'pp',
    'quiet': {
        'soloist': 'mp',
        'piano': 'p'
    },
    'loud': {
        'soloist': 'f',
        'accompanists': 'mf',
        'piano': 'mf'
    }
}
dynamics = {
    'I': dynamics_a,
    'II': dynamics_a,
    'III': {
        'drone': 'p',
        'quiet': {
            'soloist': 'mf',
            'piano': 'mp'
        },
        'loud': {
            'soloist': 'ff',
            'accompanists': 'f',
            'piano': 'f'
        }
    },
    'IV': dynamics_a
}


def make_phrase(movement, drone, volume, harmony_options):
    phrase = {}

    phrase['n_bars'] = weighted_choice(n_bars_options[movement], n_bars_weights[movement])
    phrase['soloist'] = soloist[movement]

    phrase['accompanists'] = accompanists[movement] if volume == 'loud' else None

    phrase['drone'] = drone

    phrase['dynamics'] = dynamics[movement][volume]
    phrase['dynamics']['drone'] = dynamics[movement]['drone']

    # TODO
    # phrase['harmonic_rhythm']
    # phrase['piano_rhythm']
    # phrase['soloist_rhythm']
    # if volume == 'loud':
    #     phrase['accompanists_rhythm']

    return phrase


def choose_fifth_drone():
    drone = []
    a = random.choice(drone_options)
    drone.append(a)
    drone_options.remove(a)
    b = (a + 7) % 12
    if b not in drone_options:
        b = (a + 5) % 12
        if b not in drone_options:
            raise AnimalPlayException('A fifth in either direction is not available for this drone.')
    drone.append(b)
    drone_options.remove(b)
    random.shuffle(drone)
    return drone


def get_harmony_options(drone):
    return []


def make_form():
    form = []
    for movement in ['I', 'II', 'III', 'IV']:
        for drone in [True, None]:
            if drone:
                if movement == 'III':
                    drone = try_f(choose_fifth_drone)
                else:
                    drone = random.choice(drone_options)
                    drone_options.remove(drone)
            harmony_options = get_harmony_options(drone)
            for volume in ['quiet', 'loud', 'quiet', 'loud']:
                phrase = try_f(make_phrase, args=[movement, drone, volume, harmony_options])
                # phrase = make_phrase(movement, drone, volume, harmony_options)
                form.append(phrase)
    return form


def adjust_drone_starts_and_ends(form):
    pass


def adjust_soloist_starts_and_ends(form):
    pass
