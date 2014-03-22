#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from abjad import (Measure, TimeSignature, Note, Chord, Duration, Container)

from abjad import Rest

from database import Database
from notate import notate_score, notate_parts
from score import make_score
from form import make_form
from abjad_utils import get_empty_bar, get_note, container, tie, beam


from abjad import Multiplier, Tuplet
from abjad import Beam, attach


class AnimalPlay(object):
    def __init__(self):
        self.now = datetime.datetime.utcnow()
        self.db = Database()

    def test(self):
        self.score = make_score()

        notes = [
            Note(2, Duration(1, 16)),
            Note(4, Duration(1, 16)),
            Note(5, Duration(1, 8)),
            Note(5, Duration(1, 8)),
            Tuplet(Multiplier(2, 3), [
                Note(4, Duration(1, 16)),
                Note(5, Duration(1, 16)),
                Note(4, Duration(1, 16)),
            ]),
            Note(3, Duration(1, 8)),
            Note(0, Duration(1, 8)),
            Note(0, Duration(1, 8)),
            Note(7, Duration(1, 8)),
        ]

        beam(notes[:3])
        beam(notes[3:7])
        beam(notes[7:9])
        beam(notes[9:])

        tie(notes[2:4])

        self.score['Violin'].extend(notes)
        self.notate(parts=False, midi=True)

    def generate(self):
        self.score = make_score()
        self.staves = []
        for staff in self.score:
            if staff.name == 'Piano':
                for s in staff:
                    self.staves.append(s)
            else:
                self.staves.append(staff)
        self.form = make_form()

        n = 0
        for staff in self.staves:
            print staff.name
            for phrase in self.form:
                print '-'* 20
                for _ in range(phrase['n_bars']):
                    print n
                    n += 1
                    empty = Measure(TimeSignature((4, 4)), [Rest(Duration(1, 1))])
                    staff.append(empty)




    # def generate(self):
    #     self.setup()


    #     n = 0
    #     for phrase in self.form:
    #         drone = phrase['drone']
    #         for _ in range(phrase['n_bars']):
    #             # print n
    #             n += 1
    #             for staff in self.staves:
    #                 if staff.name == 'Synthesizer' and drone != None:
    #                     note = get_note(drone, (1, 1))
    #                     bar = Measure(TimeSignature((4, 4)), [note])
    #                 else:
    #                     bar = get_empty_bar()
    #                 staff.append(bar)




    # def setup(self):
    #     self.score = make_score()

    #     self.staves = Container()
    #     self.staves.is_simultaneous = True
    #     for staff in self.score:
    #         if staff.name == 'Piano':
    #             for s in staff:
    #                 self.staves.append(s)
    #         else:
    #             self.staves.append(staff)


    #     self.form = make_form()



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
