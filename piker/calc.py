"""
Handy financial calculations.
"""
import math
import itertools


def humanize(number, digits=1):
    """Convert large numbers to something with at most 3 digits and
    a letter suffix (eg. k: thousand, M: million, B: billion).
    """
    try:
        float(number)
    except ValueError:
        return 0
    if not number or number <= 0:
        return number
    mag2suffix = {3: 'k', 6: 'M', 9: 'B'}
    mag = math.floor(math.log(number, 10))
    if mag < 3:
        return number
    maxmag = max(itertools.takewhile(lambda key: mag >= key, mag2suffix))
    return "{:.{digits}f}{}".format(
        number/10**maxmag, mag2suffix[maxmag], digits=digits)


def percent_change(init, new):
    """Calcuate the percentage change of some ``new`` value
    from some initial value, ``init``.
    """
    if not (init and new):
        return 0
    return (new - init) / init * 100.
