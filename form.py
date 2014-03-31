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
    get_bar
)
import harmonic_rhythm
from harmony import Harmony
from piano import next_piano_bass_note


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
    drone.sort()
    drone = tuple(drone)
    return drone


def choose_drones():
    options = range(12)
    drones = random.sample(options, 3)
    [options.remove(d) for d in drones]
    fifth = try_f(choose_fifth_drone, args=[options])
    drones.insert(2, fifth)
    return drones


class Form(object):
    def __init__(self, score):
        self.score = score
        self.bars = []

        self.drones = choose_drones()

        self.harmony = Harmony(self.drones)

        self.make_bars()
        self.group_sections()
        self.set_staves()

        self.adjust_soloist_entrances()

        movement = None
        for b in self.bars:
            if movement != b['movement_name']:
                movement = b['movement_name']
                print movement
            print b['soloist'], b['accompanists']

        self.temp_fill_with_rests()

        self.make_drones()
        self.make_harmonic_rhythm()
        self.choose_harmonies()
        self.make_bassline()

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
                            dynamics=Conf.dynamics[movement_number][volume[0]],
                        )
                        bar['dynamics']['drone'] = Conf.dynamics[movement_number]['drone']
                        self.bars.append(bar)
                        bar_index += 1

    def group_section(self, bars, attr):
        """Group a list of bar configs by a config attribute"""
        return [list(group) for key, group in groupby(bars, lambda x: x[attr])]

    def group_sections(self):
        self.movement_sections = self.group_section(self.bars, 'movement_number')
        self.drone_sections = self.group_section(self.bars, 'drone')
        self.volume_sections = self.group_section(self.bars, 'volume')

        self.movement_volume_sections = [self.group_section(m, 'volume') for m in self.movement_sections]

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

            piano_first_note = piano[bar_index][0]
            add_dynamic(piano_first_note, first_bar_conf['dynamics']['piano'])

        # for section in self.volume_sections:
        #     first_bar_conf = section[0]
        #     bar_index = first_bar_conf['bar_index']

        #     soloist = self.score[first_bar_conf['soloist']]
        #     soloist_first_note = soloist[bar_index][0]
        #     add_dynamic(soloist_first_note, first_bar_conf['dynamics']['soloist'])

        #     for acc_name in first_bar_conf['accompanists']:
        #         acc = self.score[acc_name]
        #         first_note = acc[bar_index][0]
        #         add_dynamic(first_note, first_bar_conf['dynamics']['accompanists'])

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
        no = ['Synthesizer', 'Piano upper', 'Piano lower']
        staves = [s for s in self.staves if s.name not in no]
        for staff in staves:
            for bar in self.bars:
                staff.append(get_rest_bar())

    def make_harmonic_rhythm(self):
        piano_upper = self.score['Piano'][0]
        for phrase in self.volume_sections:
            bars = harmonic_rhythm.choose(phrase)
            for bar in bars:
                piano_upper.append(bar)

    def choose_harmonies(self):
        piano_upper = self.score['Piano'][0]
        for bar_config in self.bars:
            drone = bar_config['drone']
            bar_index = bar_config['bar_index']

            bar_config['harmonies'] = []
            bar_config['harmonies_not_covered'] = []

            for i, dur in enumerate(bar_config['harmonic_rhythm']):
                chord = piano_upper[bar_index][i]

                harm = self.harmony.choose(drone)
                bar_config['harmonies'].append(harm)
                bar_config['harmonies_not_covered'].append(harm)
                chord.note_heads.extend(harm)

    def make_bassline(self):
        previous = -8
        piano_lower = self.score['Piano'][1]
        for bar_config in self.bars:
            harmonies = bar_config['harmonies']
            harmonic_rhythm = bar_config['harmonic_rhythm']

            pitches = []
            for i, h in enumerate(harmonies):
                p = next_piano_bass_note(previous, h)
                previous = p
                pitches.append(p)

                # bar_config['harmonies_not_covered'][i].remove(abs(p % 12))

            bar_config['piano_lower_pitches'] = pitches
            bar = get_bar(harmonic_rhythm, pitches)
            piano_lower.append(bar)

    def adjust_soloist_entrances(self):
        movements = self.movement_sections
        for i, movement in enumerate(movements):
            next_i = (i + 1) % len(movements)
            next_soloist = movements[next_i][0]['soloist']

            for bar in movements[next_i]:
                if bar['accompanists'] != ():
                    next_accompanists = bar['accompanists']
                    break

            last_section = self.movement_volume_sections[i][-1]
            for bar_config in last_section:
                bar_config['accompanists'] = next_accompanists


            # Pick soloist exit and new soloist entrance

            # No one should ever write code like this
            last_sections = self.movement_volume_sections[i][-3:]
            last_sections[0] = last_sections[0][len(last_sections[0]) / 2:]
            last_sections[-1] = last_sections[-1][:len(last_sections[-1]) / 2]

            lengths = [len(section) for section in last_sections]

            flat = []
            for section in last_sections:
                for bar in section:
                    flat.append(bar)

            exit_bar_index = random.choice(range(sum(lengths[:2])))

            for bar in flat[exit_bar_index:]:
                bar['soloist'] = None

            for bar in last_section[len(last_section) / 2:]:
                bar['soloist'] = None


            possible_entrance_bars = flat[exit_bar_index + 1:]
            entrance_bar_index = random.choice(range(len(possible_entrance_bars)))
            new_solist_bars = possible_entrance_bars[entrance_bar_index:]
            for bar in new_solist_bars:
                bar['soloist'] = next_soloist

            for bar in last_section[len(last_section) / 2:]:
                bar['soloist'] = next_soloist
