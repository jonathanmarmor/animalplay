#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from database import Database
from notate import notate_score, notate_parts, notate_Bb_clarinet_part
from score import make_score
from form import Form


class AnimalPlay(object):
    def __init__(self):
        self.now = datetime.datetime.utcnow()
        self.db = Database()

        self.score = make_score()
        self.form = Form(self.score)

    # def test(self):
    #     self.score = make_score()

    #     notes = [
    #         Note(2, Duration(1, 16)),
    #         Note(4, Duration(1, 16)),
    #         Note(5, Duration(1, 8)),
    #         Note(5, Duration(1, 8)),
    #         Tuplet(Multiplier(2, 3), [
    #             Note(4, Duration(1, 16)),
    #             Note(5, Duration(1, 16)),
    #             Note(4, Duration(1, 16)),
    #         ]),
    #         Note(3, Duration(1, 8)),
    #         Note(0, Duration(1, 8)),
    #         Note(0, Duration(1, 8)),
    #         Note(7, Duration(1, 8)),
    #     ]

    #     beam(notes[:3])
    #     beam(notes[3:7])
    #     beam(notes[7:9])
    #     beam(notes[9:])

    #     tie(notes[2:4])

    #     self.score['Violin'].extend(notes)
    #     self.notate(parts=False, midi=True)

    def notate(self, parts=True, midi=True):
        notate_score(self.score, self.now, midi=midi)
        if parts:
            notate_parts(self.score, self.now, midi=midi)
            notate_Bb_clarinet_part(self.score, self.now)

    def serialize(self):
        # TODO figure out other ways to serialize so I can reconstitute as a python object I can manipulate
        pass


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-midi', dest='midi', action='store_false',
        default=True, help='Do not make midi files.')
    parser.add_argument('--no-parts', dest='parts', action='store_false',
        default=True, help='Do not make instrument parts.')
    parser.add_argument('--score', '-s', dest='score', action='store_true',
        default=False, help='Make the score PDF only.')
    parser.add_argument('--no-notation', '-n', dest='notation', action='store_false',
        default=True, help='Do not make any notation. Just for testing.')

    args = parser.parse_args()

    if args.score:
        args.parts = False
        args.midi = False

    animalplay = AnimalPlay()
    if args.notation:
        animalplay.notate(midi=args.midi, parts=args.parts)
