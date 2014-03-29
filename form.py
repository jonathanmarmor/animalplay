# -*- coding: utf-8 -*-

import random
from itertools import groupby

from abjad import Rest

from utils import weighted_choice, try_f, AnimalPlayException
from abjad_utils import (
    get_rest_bar,
    get_one_note_bar,
    tie,
    add_rehearsal_mark,
    add_dynamic,
    add_final_barline,
    add_double_barline,
)
# import harmonic_rhythm


class Conf(object):
    movements = range(4)
    movement_names = ['I', 'II', 'III', 'IV']
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
        self.group_sections()
        self.set_staves()

        self.temp_fill_with_rests()

        self.make_drones()

        self.add_rehearsal_marks()
        self.add_dynamics()
        self.add_double_barlines()

        self.add_final_barlines()


    def make_bars(self):
        bar_index = 0
        for movement_number in Conf.movements:
            for drone in [True, None]:
                if drone:
                    drone = self.drones[movement_number]
                for volume in ['q1', 'l1', 'q2', 'l2']:
                    n_bars = weighted_choice(Conf.n_bars_options[movement_number], Conf.n_bars_weights[movement_number])
                    for bar_n in range(n_bars):
                        bar = dict(
                            movement_number=movement_number,
                            movement_name=Conf.movement_names[movement_number],
                            drone=drone,
                            volume=volume,
                            bar_index=bar_index,
                            soloist=Conf.soloist[movement_number],
                            accompanists=Conf.accompanists[movement_number] if volume.startswith('l') else (),
                            dynamics = Conf.dynamics[movement_number][volume[0]],
                        )
                        bar['dynamics']['drone'] = Conf.dynamics[movement_number]['drone']
                        self.bars.append(bar)
                        bar_index += 1

    def group_section(self, attr):
        return [list(group) for key, group in groupby(self.bars, lambda x: x[attr])]

    def group_sections(self):
        self.movement_sections = self.group_section('movement_number')
        self.drone_sections = self.group_section('drone')
        self.volume_sections = self.group_section('volume')

    def set_staves(self):
        self.staves = []
        for inst in self.score:
            if inst.name == 'Piano':
                for staff in inst:
                    self.staves.append(staff)
            else:
                self.staves.append(inst)

    def make_drones(self):
        for bars in self.drone_sections:
            drone = bars[0]['drone']
            if drone != None:
                for bar in bars:
                    bar['Synthesizer'] = get_one_note_bar(drone)
                bars = [b['Synthesizer'] for b in bars]
                tie(bars)
            else:
                for bar in bars:
                    bar['Synthesizer'] = get_rest_bar()

        synth = self.score['Synthesizer']
        synth.extend([bar['Synthesizer'] for bar in self.bars])

    def add_rehearsal_marks(self):
        for section in self.volume_sections[4::4]:
            first_bar_index = section[0]['bar_index']
            for staff in self.score:
                if staff.name == 'Piano':
                    add_rehearsal_mark(staff[0][first_bar_index])
                else:
                    add_rehearsal_mark(staff[first_bar_index])

    def add_dynamics(self):
        piano = self.score['Piano'][1]
        for section in self.volume_sections:
            first_bar_conf = section[0]
            bar_index = first_bar_conf['bar_index']

            soloist = self.score[first_bar_conf['soloist']]
            soloist_first_note = soloist[bar_index][0]
            add_dynamic(soloist_first_note, first_bar_conf['dynamics']['soloist'])

            for acc_name in first_bar_conf['accompanists']:
                acc = self.score[acc_name]
                first_note = acc[bar_index][0]
                add_dynamic(first_note, first_bar_conf['dynamics']['accompanists'])

            piano_first_note = piano[bar_index][0]
            add_dynamic(piano_first_note, first_bar_conf['dynamics']['piano'])

        synth = self.score['Synthesizer']
        # TODO use the section where the drone is actually sounding, not the square section
        for section in self.drone_sections:
            first_bar_conf = section[0]
            bar_index = first_bar_conf['bar_index']
            synth_first_note = synth[bar_index][0]
            if not isinstance(synth_first_note, Rest):
                add_dynamic(synth_first_note, first_bar_conf['dynamics']['drone'])

    def add_double_barlines(self):
        for section in self.volume_sections[:-1]:
            last_bar_conf = section[-1]
            bar_index = last_bar_conf['bar_index']
            for staff in self.staves:
                add_double_barline(staff[bar_index][-1])

    def add_final_barlines(self):
        for staff in self.staves:
            add_final_barline(staff)

    def temp_fill_with_rests(self):
        staves = [s for s in self.staves if s.name != 'Synthesizer']
        for staff in staves:
            for bar in self.bars:
                staff.append(get_rest_bar())

    # def make_harmonic_rhythm(self):
    #     self.harmonic_rhythm = []
    #     for bar in self.bars:
    #         hr = harmonic_rhythm.choose()
    #         bar['measure'] = Measure(TimeSignature((4, 4)), [Chord()])


    # def make_piano(self):
    #     pass
