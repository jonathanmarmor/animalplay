import os
import datetime
import subprocess

from abjad import attach

from abjad import lilypondfiletools
from abjad import instrumenttools
from abjad import indicatortools

from abjad import Score
from abjad import Staff, StaffGroup
from abjad import Clef


def add_tempo(thing):
    # TODO figure out the actual tempo I want for the piece
    tempo = indicatortools.Tempo((1, 4), (112, 120))
    attach(tempo, thing)


def add_time_signature(thing):
    time_signature = indicatortools.TimeSignature((4, 4))
    attach(time_signature, thing)


def get_melody_staff(music, instrument_class, instrument_name,
        short_instrument_name):
    staff = Staff(music)
    staff.name = instrument_name
    instrument = instrument_class(instrument_name=instrument_name,
        short_instrument_name=short_instrument_name)
    attach(instrument, staff)
    add_time_signature(staff)
    add_tempo(staff)
    return staff

def get_piano_staff(left_music, right_music):
    piano_staff = StaffGroup()
    piano_staff.name = 'piano'
    piano_staff.context_name = 'PianoStaff'

    upper_staff = Staff(left_music)
    upper_staff.name = 'piano upper'
    add_time_signature(upper_staff)
    add_tempo(upper_staff)

    lower_staff = Staff(right_music)
    lower_staff.name = 'piano lower'
    add_time_signature(lower_staff)
    add_tempo(lower_staff)

    piano_staff.append(upper_staff)
    piano_staff.append(lower_staff)

    piano = instrumenttools.Piano(short_instrument_name='Pno')

    attach(piano, piano_staff)
    bass_clef = Clef('bass')
    attach(bass_clef, lower_staff)
    return piano_staff


def get_synthesizer_staff(music):
    staff = Staff(music, name='Synthesizer Staff')
    clef = indicatortools.Clef('treble')
    attach(clef, staff)
    synth = instrumenttools.Instrument(
        instrument_name='Synthesizer',
        short_instrument_name='Synth'
    )
    attach(synth, staff)
    add_time_signature(staff)
    add_tempo(staff)
    return staff


def make_score():
    music = "c'4 d'4 e'4 f'4"

    violin_staff = get_melody_staff(music, instrumenttools.Violin, 'Violin',
            'Vn')
    clarinet_staff = get_melody_staff(music, instrumenttools.ClarinetInBFlat,
            'Bb Clarinet', 'Cl')
    cello_staff = get_melody_staff(music, instrumenttools.Cello, 'Cello', 'Vc')
    piano_staff = get_piano_staff(music, music)
    synth_staff = get_synthesizer_staff(music)

    score = Score([violin_staff, clarinet_staff, cello_staff, piano_staff,
            synth_staff])
    return score


def make_lilypond_file(score, title, composer):
    lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
    lilypond_file.header_block.title = title
    lilypond_file.header_block.composer = composer
    return lilypond_file


def get_filepath():
    root = '/Users/jmarmor/output/animalplay'
    now = datetime.datetime.utcnow()
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    folder = os.path.join(root, timestamp)
    os.mkdir(folder)
    filepath = os.path.join(folder, 'animalplay')
    return filepath


def main():
    score = make_score()
    title = 'Animal Play'
    composer = 'Jonathan Marmor'
    lilypond_file = make_lilypond_file(score, title, composer)
    filepath = get_filepath()

    ly_file_path = '{}.{}'.format(filepath, 'ly')
    temp_ly_file_path = '{}.tmp'.format(ly_file_path)

    with open(temp_ly_file_path, 'w') as temp_file:
        temp_file.write(format(lilypond_file))

    # Fix Piano staff label by uncommenting
    fix = {
        '%%% \set PianoStaff.instrumentName = \markup { Piano } %%%': '\set PianoStaff.instrumentName = \markup { Piano }',
        '%%% \set PianoStaff.shortInstrumentName = \markup { Pno } %%%': '\set PianoStaff.shortInstrumentName = \markup { Pno }'
    }
    f1 = open(temp_ly_file_path, 'r')
    f2 = open(ly_file_path, 'w')
    for line in f1:
        for k in fix:
            if k in line:
                line = line.replace(k, fix[k])
        f2.write(line)
    f1.close()
    f2.close()
    os.remove(temp_ly_file_path)

    process = subprocess.Popen(['lilypond', '-dno-point-and-click',
        '--output={}'.format(filepath), ly_file_path],
        shell=False)
    process.wait()

    # Make MIDI
    lilypond_file.score_block.append(lilypondfiletools.MIDIBlock())
    midi_ly_file_path = '{}-midi.{}'.format(filepath, 'ly')
    with open(midi_ly_file_path, 'w') as temp_file:
        temp_file.write(format(lilypond_file))

    process = subprocess.Popen(['lilypond',
        '--output={}'.format(filepath), midi_ly_file_path],
        shell=False)
    process.wait()
    os.remove(midi_ly_file_path)


    # TODO figure out other ways to serialize so I can reconstitute as a python object I can manipulate

    # TODO make parts too!
