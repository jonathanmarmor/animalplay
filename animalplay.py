#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from abjad import (Measure, TimeSignature, Note, Chord, Duration, Container)

from database import Database
from notate import notate_score, notate_parts
from score import make_score
from form import make_form
from abjad_utils import get_empty_bar, get_note, container


class AnimalPlay(object):
    def __init__(self):
        self.now = datetime.datetime.utcnow()
        self.db = Database()

    def generate(self):
        self.setup()


        n = 0
        for phrase in self.form:
            drone = phrase['drone']
            for _ in range(phrase['n_bars']):
                # print n
                n += 1
                for staff in self.staves:
                    if staff.name == 'Synthesizer' and drone != None:
                        note = get_note(drone, (1, 1))
                        bar = Measure(TimeSignature((4, 4)), [note])
                    else:
                        bar = get_empty_bar()
                    staff.append(bar)




    def setup(self):
        self.score = make_score()

        self.staves = Container()
        self.staves.is_simultaneous = True
        for staff in self.score:
            if staff.name == 'Piano':
                for s in staff:
                    self.staves.append(s)
            else:
                self.staves.append(staff)


        self.form = make_form()



    def notate(self, parts=True, midi=True):
        notate_score(self.score, self.now, midi=midi)
        if parts:
            notate_parts(self.score, self.now, midi=midi)

    def serialize(self):
        # TODO figure out other ways to serialize so I can reconstitute as a python object I can manipulate
        pass


def run(parts=True, midi=True):
    animalplay = AnimalPlay()
    animalplay.generate()
    animalplay.notate(midi=midi, parts=parts)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-midi', dest='midi', action='store_false',
        default=True, help='Do not make midi files.')
    parser.add_argument('--no-parts', dest='parts', action='store_false',
        default=True, help='Do not make instrument parts.')
    parser.add_argument('--score', '-s', dest='score', action='store_true',
        default=False, help='Make the score PDF only.')
    args = parser.parse_args()

    if args.score:
        args.parts = False
        args.midi = False

    run(parts=args.parts, midi=args.midi)
