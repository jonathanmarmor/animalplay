# -*- coding: utf-8 -*-

import random
from itertools import groupby

from abjad import Rest

from utils import weighted_choice, try_f, AnimalPlayException, group_into_bars
from abjad_utils import (
    get_rest_bar,
    get_one_note_bar,
    tie,
    add_rehearsal_mark,
    add_dynamic,
    add_final_barline,
    add_double_barline,
    get_bar,
    is_rest,
    parse_rhythm,
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
    n_bars_options = ((8, 4), (8, 4, 2), (4, 8,  16, 2), (8, 2, 4))
    n_bars_weights = ((1, 1), (8, 7, 1), (5, 16, 10, 1), (3, 3, 2))

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

        self.temp_fill_with_rests()

        self.make_harmonic_rhythm()

        self.make_drones()

        self.choose_harmonies()
        self.make_bassline()

        # self.make_accompaniment()

        # self.make_soloist()

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

        self.harmonic_rhythm = []
        self.raw_harmonic_rhythm = []
        self.harmonic_rhythm_drones = []
        self.harmonies = []

    def set_staves(self):
        self.staves = []
        for inst in self.score:
            if inst.name == 'Piano':
                for staff in inst:
                    self.staves.append(staff)
            else:
                self.staves.append(inst)

    def add_rehearsal_marks(self):
        for section in self.volume_sections[4::4]:
            first_bar_index = section[0]['bar_index']
            for staff in self.score:
                if staff.name == 'Piano':
                    add_rehearsal_mark(staff[0][first_bar_index])
                else:
                    add_rehearsal_mark(staff[first_bar_index])

    def add_piano_dynamics(self):
        piano = self.score['Piano'][1]
        for section in self.volume_sections:
            first_bar_conf = section[0]
            bar_index = first_bar_conf['bar_index']

            piano_first_note = piano[bar_index][0]
            add_dynamic(piano_first_note, first_bar_conf['dynamics']['piano'])

    def add_soloist_dynamics(self):
        dynamic = None
        previous_soloist = None
        for bar in self.bars:
            i = bar['bar_index']
            soloist_name = bar['soloist']
            if soloist_name:
                dyn = bar['dynamics']['soloist']
                if dyn != dynamic or soloist_name != previous_soloist:
                    dynamic = dyn
                    previous_soloist = soloist_name
                    soloist = self.score[soloist_name]
                    first_note = soloist[i][0]
                    add_dynamic(first_note, dynamic)

    def add_accompanists_dynamics(self):
        for section in self.volume_sections:
            first_bar_conf = section[0]
            bar_index = first_bar_conf['bar_index']
            for acc_name in first_bar_conf['accompanists']:
                acc = self.score[acc_name]
                first_note = acc[bar_index][0]
                add_dynamic(first_note, first_bar_conf['dynamics']['accompanists'])

    def add_synth_dynamics(self):
        synth = self.score['Synthesizer']
        # TODO use the section where the drone is actually sounding, not the square section
        for section in self.drone_sections:
            first_bar_conf = section[0]
            bar_index = first_bar_conf['bar_index']
            synth_first_note = synth[bar_index][0]
            if not isinstance(synth_first_note, Rest):
                add_dynamic(synth_first_note, first_bar_conf['dynamics']['drone'])

    def add_dynamics(self):
        self.add_piano_dynamics()
        self.add_soloist_dynamics()
        self.add_accompanists_dynamics()
        self.add_synth_dynamics()

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
            raw, bars = harmonic_rhythm.choose(phrase)
            self.raw_harmonic_rhythm.append(raw)
            self.harmonic_rhythm.append(bars)
            for bar in bars:
                piano_upper.append(bar)

    def choose_harmonies(self):
        piano_upper = self.score['Piano'][0]
        for drone, rhythm in zip(self.harmonic_rhythm_drones, self.raw_harmonic_rhythm):
            pitches = [self.harmony.choose(d) for d in drone]
            self.harmonies.append(pitches)
            bars = parse_rhythm(rhythm, pitches=pitches)
            piano_upper.extend(bars)

    def make_bassline(self):
        previous = -8
        piano_lower = self.score['Piano'][1]
        for harmonies, rhythm in zip(self.harmonies, self.raw_harmonic_rhythm):
            pitches = []
            for h in harmonies:
                p = next_piano_bass_note(previous, h)
                previous = p
                pitches.append(p)
            bars = parse_rhythm(rhythm, pitches)
            piano_lower.extend(bars)

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

    def make_accompaniment(self):
        for bar_config in self.bars:
            accompanists = bar_config['accompanists']
            if accompanists:
                a_name, b_name = accompanists
                a = self.score[a_name]
                b = self.score[b_name]

                harmonies = bar_config['harmonies']
                harmonic_rhythm = bar_config['harmonic_rhythm']

                a_pitches = []
                b_pitches = []
                for i, h in enumerate(harmonies):
                    a_pitch = random.choice(h)
                    a_pitches.append(a_pitch)
                    b_pitch = random.choice(h)
                    b_pitches.append(b_pitch)

                bar_config['{}_pitches'.format(a_name)] = a_pitches
                bar_config['{}_pitches'.format(b_name)] = b_pitches

                a[bar_config['bar_index']] = get_bar(harmonic_rhythm, a_pitches)
                b[bar_config['bar_index']] = get_bar(harmonic_rhythm, b_pitches)

    def make_soloist(self):
        for bar_config in self.bars:
            name = bar_config['soloist']
            if name:
                soloist = self.score[name]

                harmonies = bar_config['harmonies']
                harmonic_rhythm = bar_config['harmonic_rhythm']

                pitches = []
                for i, h in enumerate(harmonies):
                    pitch = random.choice(h)
                    pitches.append(pitch)

                bar_config['{}_pitches'.format(name)] = pitches

                soloist[bar_config['bar_index']] = get_bar(harmonic_rhythm, pitches)

    def make_drones(self):
        synth = self.score['Synthesizer']

        # Drone 1
        bars = [get_one_note_bar(self.drones[0]) for _ in self.drone_sections[0]]
        tie(bars)
        synth.extend(bars)

        for rhythm in self.raw_harmonic_rhythm[:4]:
            self.harmonic_rhythm_drones.append([self.drones[0] for r in rhythm])

        # Rest 1
        rest_bars = [get_rest_bar() for _ in self.drone_sections[1]]
        synth.extend(rest_bars)

        for rhythm in self.raw_harmonic_rhythm[4:8]:
            self.harmonic_rhythm_drones.append([None for r in rhythm])


        # Drone 2
        bars = [get_one_note_bar(self.drones[1]) for _ in self.drone_sections[2]]
        tie(bars)
        synth.extend(bars)

        for rhythm in self.raw_harmonic_rhythm[8:12]:
            self.harmonic_rhythm_drones.append([self.drones[1] for r in rhythm])


        #######################################
        #### Rest 2 and Drone 3 A entrance ####
        #######################################

        # First two volume sections are resting
        rest_bars = []
        for section in self.volume_sections[12:14]:
            rest_bars.extend([get_rest_bar() for _ in section])

        for rhythm in self.raw_harmonic_rhythm[12:14]:
            self.harmonic_rhythm_drones.append([None for r in rhythm])

        # The drone comes in at a random point in the third volume section

        drone_3a = self.drones[2][0]

        entrance_section = self.raw_harmonic_rhythm[14]
        start = random.choice(range(len(entrance_section) - 1))

        rests = ['r' for duration in entrance_section[:start]]
        drones = [drone_3a for duration in entrance_section[start:]]

        pitches = rests + drones
        entrance_bars = parse_rhythm(entrance_section, pitches=pitches)

        rhythm = []
        for pitch in pitches:
            if pitch == 'r':
                rhythm.append(None)
            else:
                rhythm.append(drone_3a)
        self.harmonic_rhythm_drones.append(rhythm)

        # Last volume section is droning
        drone_bars = [get_one_note_bar(drone_3a) for _ in self.volume_sections[15]]

        self.harmonic_rhythm_drones.append([drone_3a for dur in self.raw_harmonic_rhythm[15]])

        synth.extend(rest_bars + entrance_bars + drone_bars)

        to_tie = entrance_bars + drone_bars

        # TODO ties


        #######################
        #### Drone 3 A & B ####
        #######################

        # First volume section is drone 3 A
        bars_1 = [get_one_note_bar(drone_3a) for _ in self.volume_sections[16]]
        self.harmonic_rhythm_drones.append([drone_3a for dur in self.raw_harmonic_rhythm[16]])


        # Second volume section drone 3 B comes in
        entrance_section = self.raw_harmonic_rhythm[17]
        start = random.choice(range(1, len(entrance_section)))

        a = [drone_3a for duration in entrance_section[:start]]
        both = [self.drones[2] for duration in entrance_section[start:]]

        pitches = a + both
        bars_2 = parse_rhythm(entrance_section, pitches=pitches)

        self.harmonic_rhythm_drones.append(pitches)


        # Third and Fourth volume sections both drones
        bars_3_4 = []
        for section in self.volume_sections[18:20]:
            bars_3_4.extend([get_one_note_bar(self.drones[2]) for _ in section])

        for rhythm in self.raw_harmonic_rhythm[18:20]:
            self.harmonic_rhythm_drones.append([self.drones[2] for dur in rhythm])


        # Fifth volume section drone 3 A exits
        drone_3b = self.drones[2][1]

        exit_section = self.raw_harmonic_rhythm[20]
        start = random.choice(range(1, len(exit_section)))

        both = [self.drones[2] for duration in exit_section[:start]]
        b = [drone_3b for duration in exit_section[start:]]

        pitches = both + b
        bars_5 = parse_rhythm(exit_section, pitches=pitches)

        self.harmonic_rhythm_drones.append(pitches)


        # Sixth volume section is drone 3 B
        bars_6 = [get_one_note_bar(drone_3b) for _ in self.volume_sections[21]]
        self.harmonic_rhythm_drones.append([drone_3b for dur in self.raw_harmonic_rhythm[21]])


        # Seventh volume section drone 3 B exits
        exit_section = self.raw_harmonic_rhythm[22]
        start = random.choice(range(1, len(exit_section)))

        b = [drone_3b for duration in exit_section[:start]]
        rest = ['r' for duration in exit_section[start:]]

        pitches = b + rest
        bars_7 = parse_rhythm(exit_section, pitches=pitches)


        rhythm_drones = []
        for p in pitches:
            if p == 'r':
                rhythm_drones.append(None)
            else:
                rhythm_drones.append(p)
        self.harmonic_rhythm_drones.append(rhythm_drones)


        # Eighth volume section is resting
        bars_8 = [get_rest_bar() for _ in self.volume_sections[23]]
        self.harmonic_rhythm_drones.append([None for dur in self.raw_harmonic_rhythm[23]])


        bars = bars_1 + bars_2 + bars_3_4 + bars_5 + bars_6 + bars_7 + bars_8
        synth.extend(bars)

        to_tie += bars
        tie(to_tie)


        # Drone 4
        bars = [get_one_note_bar(self.drones[3]) for _ in self.drone_sections[6]]
        tie(bars)
        synth.extend(bars)

        for rhythm in self.raw_harmonic_rhythm[24:28]:
            self.harmonic_rhythm_drones.append([self.drones[3] for r in rhythm])

        # Rest 4
        bars = [get_rest_bar() for _ in self.drone_sections[7]]
        synth.extend(bars)

        for rhythm in self.raw_harmonic_rhythm[28:]:
            self.harmonic_rhythm_drones.append([None for r in rhythm])
