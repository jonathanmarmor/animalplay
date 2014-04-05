# -*- coding: utf-8 -*-

from abjad import attach
from abjad import abjad_configuration
from abjad import Score, StaffGroup, Staff, Clef
from abjad.tools.indicatortools import Tempo
from abjad.tools.instrumenttools import (Violin, ClarinetInBFlat, Cello, Piano,
    Instrument)

from config import Config


def add_tempo(thing, duration=None, bpm_range=None):
    if not duration:
        duration = Config.tempo_duration
    if not bpm_range:
        bpm_range = Config.tempo_bpm_range
    tempo = Tempo(duration, bpm_range)
    attach(tempo, thing)


def add_time_signature(thing, numerator=4, denominator=4):
    pass
    # time_signature = TimeSignature((numerator, denominator))
    # attach(time_signature, thing)


def get_melody_staff(instrument_class, instrument_name, short_instrument_name):
    staff = Staff([])
    staff.name = instrument_name
    instrument = instrument_class(instrument_name=instrument_name,
        short_instrument_name=short_instrument_name)
    attach(instrument, staff)
    add_time_signature(staff)
    add_tempo(staff)
    return staff

def get_piano_staff():
    piano_staff = StaffGroup()
    piano_staff.name = 'Piano'
    piano_staff.context_name = 'PianoStaff'

    upper_staff = Staff([])
    upper_staff.name = 'Piano upper'
    add_time_signature(upper_staff)
    add_tempo(upper_staff)

    lower_staff = Staff([])
    lower_staff.name = 'Piano lower'
    add_time_signature(lower_staff)
    add_tempo(lower_staff)

    piano_staff.append(upper_staff)
    piano_staff.append(lower_staff)

    piano = Piano(short_instrument_name='Pno')

    attach(piano, piano_staff)
    bass_clef = Clef('bass')
    attach(bass_clef, lower_staff)
    return piano_staff


def get_synthesizer_staff():
    staff = Staff([], name='Synthesizer Staff')
    staff.name = 'Synthesizer'
    clef = Clef('treble')
    attach(clef, staff)
    synth = Instrument(
        instrument_name='Synthesizer',
        short_instrument_name='Syn'
    )
    attach(synth, staff)
    add_time_signature(staff)
    add_tempo(staff)
    return staff


def make_score():
    abjad_configuration['accidental_spelling'] = 'flats'

    violin_staff = get_melody_staff(Violin, 'Violin', 'Vn')
    clarinet_staff = get_melody_staff(ClarinetInBFlat, 'Bb Clarinet', 'Cl')
    cello_staff = get_melody_staff(Cello, 'Cello', 'Vc')
    piano_staff = get_piano_staff()
    synth_staff = get_synthesizer_staff()

    score = Score([violin_staff, clarinet_staff, cello_staff, piano_staff,
            synth_staff])
    return score
