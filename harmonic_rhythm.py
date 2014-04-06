# -*- coding: utf-8 -*-

from collections import defaultdict
import random

from utils import weighted_choice, exp_weights, break_down
from parse_rhythm import parse_rhythm


class HarmonicRhythm(object):
    def __init__(self):
        self.history = []
        self.OPTIONS = defaultdict(list)
        self.WEIGHTS = defaultdict(list)
        self.OPTIONS[1] = [
            [8, 8],
            [12, 4],
            [16],
            [8, 4, 4],
            [4, 12],
            [4, 4, 8],
            [4, 8, 4],
            [4, 4, 4, 4],
        ]
        self.WEIGHTS[1] = exp_weights(len(self.OPTIONS[1]), exponent=1.5)

        self.OPTIONS[2] = [
            [12, (4, 8), 8],
            [8, (8, 4), 12],
            [(16, 8), 8],
            [8, (8, 12), 4],
            [(16, 12), 4],
            [(16, 8), 4, 4],
            [12, (4, 4), 12],
            [8, (8, 8), 8],
            [8, (8, 16)],
            [(16, 4), 12],
            [12, (4, 16)],
            [(16, 16)],
            [4, (12, 16)],
            [8, (8, 4), 8, 4],
            [(16, 4), 8, 4],
            [8, (8, 4), 4, 8],
            [(16, 4), 4, 8],
            [8, (8, 8), 4, 4],
            [4, (12, 8), 8],
            [4, 4, (8, 8), 8],
            [4, (12, 4), 12],
            [12, (4, 8), 4, 4],
            [4, 8, (4, 16)],
            [4, 4, (8, 4), 12],
            [4, 4, (8, 16)],
            [(16, 4), 4, 4, 4],
            [4, (12, 12), 4],
            [4, (12, 8), 4, 4],
            [4, 4, (8, 12), 4],
            [4, 4, 4, (4, 16)],
            [4, (12, 4), 8, 4],
            [4, (12, 4), 4, 8],
            [4, 4, 4, (4, 4), 12],
            [12, (4, 4), 4, 4, 4],
            [4, 8, (4, 4), 4, 8],
            [4, 8, (4, 4), 8, 4],
            [8, 4, (4, 4), 4, 8],
            [8, 4, (4, 4), 8, 4],
            [8, (8, 4), 4, 4, 4],
            [4, 4, (8, 4), 8, 4],
            [4, 4, (8, 4), 4, 8],
            [4, (12, 4), 4, 4, 4],
            [4, 4, (8, 4), 4, 4, 4],
            [4, 4, 4, (4, 8), 4, 4],
            [4, 4, 4, (4, 4), 4, 8],
            [4, 4, 4, (4, 4), 8, 4],
            [4, 8, (4, 4), 4, 4, 4],
            [8, 4, (4, 4), 4, 4, 4],
            [4, 4, 4, (4, 4), 4, 4, 4],


            # # 7
            # [4, 4, 4, (4, 4), 4, 4, 4],

            # # 6
            # [4, 4, (8, 4), 4, 4, 4],
            # [4, 4, 4, (4, 8), 4, 4],
            # [4, 4, 4, (4, 4), 4, 8],
            # [4, 4, 4, (4, 4), 4, 8],
            # [4, 4, 4, (4, 4), 8, 4],
            # [4, 8, (4, 4), 4, 4, 4],
            # [8, 4, (4, 4), 4, 4, 4],

            # # 5
            # [4, 4, 4, (4, 4), 12],
            # [12, (4, 4), 4, 4, 4],
            # [4, 8, (4, 4), 4, 8],
            # [4, 8, (4, 4), 8, 4],
            # [8, 4, (4, 4), 4, 8],
            # [8, 4, (4, 4), 8, 4],
            # [8, (8, 4), 4, 4, 4],
            # [4, 4, (8, 4), 8, 4],
            # [4, 4, (8, 4), 4, 8],
            # [4, (12, 4), 4, 4, 4],

            # # 4
            # [(16, 4), 4, 4, 4],
            # [4, (12, 8), 4, 4],
            # [4, 4, (8, 12), 4],
            # [4, 4, 4, (4, 16)],
            # [4, (12, 4), 8, 4],
            # [4, (12, 4), 4, 8],
            # [8, (8, 8), 4, 4],
            # [4, 4, (8, 8), 8],
            # [8, (8, 4), 8, 4],
            # [8, (8, 4), 4, 8],
            # [12, (4, 8), 4, 4],
            # [4, 4, (8, 4), 12],

            # # 3
            # [(16, 8), 4, 4],
            # [(16, 4), 8, 4],
            # [(16, 4), 4, 8],
            # [12, (4, 4), 8],
            # [12, (4, 8), 4],
            # [8, (8, 12), 4],
            # [8 (8, 8), 8],
            # [8, (8, 4), 12],
            # [4, (12, 12), 4],
            # [4, (12, 8), 8],
            # [4, (12, 4), 12],
            # [4, 8, (4, 16)],
            # [4, 4, (8, 16)],

            # # 2
            # [(16, 12), 4],
            # [4, (12, 16)],
            # [(16, 8), 8],
            # [8, (8, 16)],
            # [(16, 4), 12],
            # [12, (4, 16)],

            # # 1
            # [(16, 16)],

        ]
        self.WEIGHTS[2] = exp_weights(len(self.OPTIONS[2]), exponent=1.2)

        # Make sure the data is good
        # for x in [1, 2]:
        #     assert len(self.OPTIONS[x]) == len(self.WEIGHTS[x])
        #     for option in self.OPTIONS[x]:
        #         total = 0
        #         for duration in option:
        #             if isinstance(duration, tuple):
        #                 duration = sum(duration)
        #             total += duration
        #         if not total == (x * 16):
        #             print x, option

    def _choose_subdivisions(self, n_bars):
        """The order of one and two bar rhythms that will make up the rhythm."""
        ones_and_twos = break_down(n_bars)
        choice = random.choice(ones_and_twos)
        random.shuffle(choice)
        return choice

    def make_rhythm(self, n_bars):
        rhythm = []
        subdivisions = self._choose_subdivisions(n_bars)
        for n in subdivisions:
            choice = weighted_choice(self.OPTIONS[n], self.WEIGHTS[n])
            rhythm.extend(choice)

        # Make sure this rhythm is the right length
        # total = 0
        # for duration in rhythm:
        #     if isinstance(duration, tuple):
        #         duration = sum(duration)
        #     total += duration
        # if total != (n_bars * 16):
        #     print 'Whoa! Wrong length.', n_bars, total, subdivisions, rhythm
        #     raise Exception()

        return rhythm

    def parse_rhythm(self, raw_rhythm):
        return parse_rhythm(raw_rhythm)

    def choose(self, section):
        """Keeping this for backwards compatibility."""
        n_bars = len(section)
        raw = self.make_rhythm(n_bars)
        rhythm = self.parse_rhythm(raw)
        return raw, rhythm
