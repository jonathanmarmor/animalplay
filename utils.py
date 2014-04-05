# -*- coding: utf-8 -*-

import random
import itertools
from collections import Counter

from matplotlib import pyplot


class AnimalPlayException(Exception):
    pass


def scale(x, minimum, maximum, floor=0, ceiling=1):
    return ((ceiling - floor) * (float(x) - minimum))/(maximum - minimum) + floor


def scale_list(l, floor=0, ceiling=1):
    minimum = 0
    maximum = sum(l)
    return [scale(x, minimum, maximum, floor, ceiling) for x in l]


def weighted_choice(options, weights):
    rand = random.random()
    rand = scale(rand, 0, 1, 0, sum(weights))
    total = 0
    for i, weight in enumerate(weights):
        total += weight
        if rand < total:
            return options[i]


MAX_DEPTH = 1000

def try_f(f, args=[], kwargs={}, depth=0):
    """Dumb way to try a random process a bunch of times."""
    depth += 1
    try:
        return f(*args, **kwargs)
    except Exception as e:
        if depth == MAX_DEPTH:
            print "Tried {} {} times. That's too many times.".format(f.__name__, MAX_DEPTH)
            raise e
        print 'trying {} again'.format(f.__name__)
        return try_f(f, args=args, kwargs=kwargs, depth=depth)


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2,s3), ..."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


def rand_tri(low=0, high=1):
    """Get a random float between low and high but closer to high"""
    mode = (high - low) / 2.0
    n = random.triangular(low, high, mode)
    if n > mode:
        n = high - n
    return scale(n, low, mode, low, high)


def rand_exp(lambd, high=None, depth=0):
    lambd = 1 / lambd
    if not high:
        high = lambd
    r = random.expovariate(lambd)
    if r > lambd:
        depth += 1
        if depth < MAX_DEPTH:
            return rand_exp(lambd)
        else:
            raise AnimalPlayException('tried rand_exp too many times.')
    return r


def plot(x, y):
    pyplot.plot(x, y)
    pyplot.show()


def deciles(numbers):
    c = Counter()
    for n in numbers:
        c[str(n)[:4]] += 1
    items = sorted(c.items(), key=lambda x: x[0])
    buckets, counts = zip(*items)
    return buckets, counts


def remove_ties(raw_rhythm):
    """
    >>> remove_ties([12, (4, 8), 8])
    [12, 4, 8, 8]
    """
    rv = []
    for duration in raw_rhythm:
        if isinstance(duration, tuple):
            rv.extend(duration)
        else:
            rv.append(duration)
    return rv


def group_into_bars(raw_rhythm, denominator=16):
    """
    >>> group_into_bars([12, (4, 8), 8])
    [[12, 4], [8, 8]]
    """
    rv = []
    untied = remove_ties(raw_rhythm)
    total = 0
    for d in untied:
        if total % denominator == 0:
            bar = []
            rv.append(bar)
        bar.append(d)
        total += d
    return rv


def exp_weights(n, exponent=2, reverse=True):
    weights = [(x + 1) ** exponent for x in range(n)]
    weights.reverse()
    return weights


def get_interval_class(a, b):
    """Returns the interval class between two pitches as a number between 0 and 6.

    >>> get_interval_class(0, 5)
    5

    >>> get_interval_class(0, 7)
    5

    >>> get_interval_class(5, 0)
    5

    >>> get_interval_class(7, 0)
    5

    >>> get_interval_class(12, 5)
    5

    >>> get_interval_class(5, 12)
    5

    >>> get_interval_class(12, 7)
    5

    >>> get_interval_class(7, 12)
    5



    >>> get_interval_class(1, 6)
    5

    >>> get_interval_class(1, 8)
    5

    >>> get_interval_class(6, 1)
    5

    >>> get_interval_class(8, 1)
    5

    >>> get_interval_class(13, 6)
    5

    >>> get_interval_class(6, 13)
    5

    >>> get_interval_class(13, 8)
    5

    >>> get_interval_class(8, 13)
    5


    >>> get_interval_class(20, 13)
    5

    >>> get_interval_class(20, -11)
    5

    >>> get_interval_class(-11, 20)
    5

    >>> get_interval_class(-11, -4)
    5

    >>> get_interval_class(-23, -16)
    5

    """
    a = a % 12
    b = b % 12
    interval = abs(a - b)
    if interval > 6:
        interval = 12 - interval
    return interval


if __name__ == '__main__':
    import doctest
    doctest.testmod()
