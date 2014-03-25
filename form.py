# -*- coding: utf-8 -*-

import random
from itertools import groupby

from utils import weighted_choice, try_f, AnimalPlayException
from abjad_utils import get_rest_bar, get_one_note_bar, tie
import harmonic_rhythm


class Conf(object):
    movements = range(4)
    soloist = ('Violin', 'Violin', 'Bb Clarinet', 'Cello')
    accompanists = (('Bb Clarinet', 'Cello'), ('Bb Clarinet', 'Cello'),
        ('Violin', 'Cello'), ('Bb Clarinet', 'Violin'))
    n_bars_options = ((8, 4), (8, 4, 2), (4, 8, 16, 2), (8, 2, 4))
    n_bars_weights = ((1, 1), (8, 7, 1), (14, 11, 6, 1), (3, 3, 2))

    dynamics_a = {
        'drone': 'pp',
        'q': {
            'soloist': 'mp',
            'piano': 'p'
        },
        'l': {
            'soloist': 'f',
            'accompanists': 'mf',
            'piano': 'mf'
        }
    }
    dynamics_b = {
        'drone': 'p',
        'q': {
            'soloist': 'mf',
            'piano': 'mp'
        },
        'l': {
            'soloist': 'ff',
            'accompanists': 'f',
            'piano': 'f'
        }
    }
    dynamics = [dynamics_a, dynamics_a, dynamics_b, dynamics_a]


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


class Form(object):
    def __init__(self, score):
        self.score = score
        self.bars = []

        self.drones = choose_drones()

        self.make_bars()
        self.make_drones()


    def make_bars(self):
        self.bars = []
        for movement_number in Conf.movements:
            for drone in [True, None]:
                if drone:
                    drone = self.drones[movement_number]
                for volume in ['q1', 'l1', 'q2', 'l2']:
                    n_bars = weighted_choice(Conf.n_bars_options[movement_number], Conf.n_bars_weights[movement_number])
                    for bar_number in range(n_bars):
                        d = dict(
                            movement_number=movement_number,
                            drone=drone,
                            volume=volume,
                            bar_number=bar_number,
                            soloist=Conf.soloist[movement_number],
                            accompanists=Conf.accompanists[movement_number] if volume.startswith('l') else (),
                            dynamics = Conf.dynamics[movement_number][volume[0]],
                        )
                        d['dynamics']['drone'] = Conf.dynamics[movement_number]['drone']
                        self.bars.append(d)

    def make_drones(self):
        for drone, bars in groupby(self.bars, lambda x: x['drone']):
            if drone != None:
                bars = list(bars)
                for bar in bars:
                    bar['measure'] = get_one_note_bar(bar['drone'])
                bars = [b['measure'] for b in bars]
                tie(bars)
            else:
                for bar in bars:
                    bar['measure'] = get_rest_bar()

        synth = self.score['Synthesizer']
        synth.extend([bar['measure'] for bar in self.bars])

    # def make_harmonic_rhythm(self):
    #     self.harmonic_rhythm = []
    #     for bar in self.bars:
    #         hr = harmonic_rhythm.choose()
    #         bar['measure'] = Measure(TimeSignature((4, 4)), [Chord()])


    # def make_piano(self):
    #     pass

