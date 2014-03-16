# -*- coding: utf-8 -*-

import random

from utils import weighted_choice, try_f, AnimalPlayException

movements = range(4)
soloist = ('Violin', 'Violin', 'Bb Clarinet', 'Cello')
accompanists = (('Bb Clarinet', 'Cello'), ('Bb Clarinet', 'Cello'),
    ('Violin', 'Cello'), ('Bb Clarinet', 'Violin'))
n_bars_options = ((8, 4), (8, 4, 2), (4, 8, 16, 2), (8, 2, 4))
n_bars_weights = ((1, 1), (8, 7, 1), (14, 11, 6, 1), (3, 3, 2))

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
dynamics_b = {
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
}
dynamics = [dynamics_a, dynamics_a, dynamics_b, dynamics_a]


def make_phrase(movement, drone, volume, harmony_options):
    phrase = {}

    phrase['n_bars'] = weighted_choice(n_bars_options[movement], n_bars_weights[movement])
    phrase['soloist'] = soloist[movement]

    phrase['accompanists'] = accompanists[movement] if volume == 'loud' else ()

    phrase['drone'] = drone

    phrase['dynamics'] = dynamics[movement][volume]
    phrase['dynamics']['drone'] = dynamics[movement]['drone']

    # TODO
    # phrase['harmonic_rhythm'] = harmonic_rhythm.choose(phrase['n_bars'])
    # phrase['piano_rhythm']
    # phrase['soloist_rhythm']
    # if volume == 'loud':
    #     phrase['accompanists_rhythm']

    return phrase


def choose_fifth_drone(options):
    options = options[:]
    drone = []
    a = random.choice(options)
    drone.append(a)
    options.remove(a)
    b = (a + 7) % 12
    if b not in options:
        b = (a + 5) % 12
        if b not in options:
            raise AnimalPlayException('A fifth in either direction is not available for this drone.')
    drone.append(b)
    random.shuffle(drone)
    return drone


def choose_drones():
    options = range(12)
    drones = random.sample(options, 3)
    [options.remove(d) for d in drones]
    fifth = try_f(choose_fifth_drone, args=[options])
    random.shuffle(fifth)
    drones.insert(2, fifth)
    return drones


def get_harmony_options(drone):
    return []


def make_form():
    drones = choose_drones()
    form = []
    for movement in movements:
        for drone in [True, None]:
            if drone:
                drone = drones[movement]
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
