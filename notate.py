# -*- coding: utf-8 -*-

import os
import subprocess

from abjad import lilypondfiletools
from abjad.tools.markuptools import Markup


def make_lilypond_file(score, now, subtitle=None):
    title = 'Animal Play'
    composer = 'Jonathan Marmor'

    lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
    lilypond_file.header_block.title = Markup(title)
    if subtitle:
        lilypond_file.header_block.subtitle = Markup(subtitle)
    lilypond_file.header_block.composer = Markup(composer)

    footer_title = title
    if subtitle:
        footer_title = '{} - {}'.format(subtitle, title)
    footer_message = '{} - {}'.format(footer_title, now.strftime('%Y-%m-%d %H:%M:%S'))
    footer_markup = """\\column {{
        \\fill-line {{ \\teeny {{ "{}" }} }}
    }}""".format(footer_message)
    lilypond_file.paper_block.oddFooterMarkup = Markup(footer_markup)
    lilypond_file.paper_block.evenFooterMarkup = Markup(footer_markup)

    return lilypond_file


def get_output_folder(now):
    root = os.path.join(os.path.expanduser('~'), 'output', 'animalplay')
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    folder = os.path.join(root, timestamp)
    if not os.path.isdir(folder):
        os.makedirs(folder)
    return folder


def get_filepath(now):
    folder = get_output_folder(now)
    filepath = os.path.join(folder, 'animalplay')
    return filepath


def fix_piano_label(ly_file_path):
    with open(ly_file_path, 'r') as f:
        text = f.read()
    os.remove(ly_file_path)

    name_a = '%%% \set PianoStaff.instrumentName = \markup { Piano } %%%'
    name_b = '\set PianoStaff.instrumentName = \markup { Piano }'
    short_name_a = '%%% \set PianoStaff.shortInstrumentName = \markup { Pno } %%%'
    short_name_b = '\set PianoStaff.shortInstrumentName = \markup { Pno }'
    text = text.replace(name_a, name_b)
    text = text.replace(short_name_a, short_name_b)

    with open(ly_file_path, 'w') as f:
        text = f.write(text)


def make_pdf(ly_file_path, output_filepath):
    process = subprocess.Popen(['lilypond', '-dno-point-and-click',
        '--output={}'.format(output_filepath), ly_file_path], shell=False)
    process.wait()


def make_midi(lilypond_file, output_filepath):
    lilypond_file.score_block.append(lilypondfiletools.MIDIBlock())
    midi_ly_file_path = '{}-midi.{}'.format(output_filepath, 'ly')
    with open(midi_ly_file_path, 'w') as temp_file:
        temp_file.write(format(lilypond_file))

    process = subprocess.Popen(['lilypond',
        '--output={}'.format(output_filepath), midi_ly_file_path], shell=False)
    process.wait()
    os.remove(midi_ly_file_path)


def get_parts_filepath(now):
    folder = get_output_folder(now)
    parts_folder = os.path.join(folder, 'parts')
    os.mkdir(parts_folder)
    filepath = os.path.join(parts_folder, 'animalplay')
    return filepath


def notate_score(score, now, midi=True):
    lilypond_file = make_lilypond_file(score, now)
    filepath = get_filepath(now)
    ly_file_path = '{}.{}'.format(filepath, 'ly')

    # Write Lilypond file
    with open(ly_file_path, 'w') as file_handle:
        file_handle.write(format(lilypond_file))

    fix_piano_label(ly_file_path)

    make_pdf(ly_file_path, filepath)

    if midi:
        make_midi(lilypond_file, filepath)


def notate_parts(score, now, midi=True):
    base_filepath = get_parts_filepath(now)
    for staff in score:
        lilypond_file = make_lilypond_file(staff, now, subtitle=staff.name)

        filepath = '{}-{}'.format(base_filepath, staff.name)
        ly_file_path = '{}.{}'.format(filepath, 'ly')

        # Write Lilypond file
        with open(ly_file_path, 'w') as file_handle:
            file_handle.write(format(lilypond_file))

        if staff.name == 'Piano':
            fix_piano_label(ly_file_path)

        make_pdf(ly_file_path, filepath)

        if midi:
            make_midi(lilypond_file, filepath)
