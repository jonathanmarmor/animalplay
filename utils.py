import random


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
        return try_f(f, args=args, kwargs=kwargs, depth=depth)
