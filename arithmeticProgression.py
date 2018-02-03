"""
Test of `ArithmeticProgression`
    >>> ap = ArithmeticProgression(0, 1, 3)
    >>> list(ap)
    [0, 1, 2]
    >>> ap = ArithmeticProgression(1, .5, 3)
    >>> list(ap)
    [1.0, 1.5, 2.0, 2.5]
    >>> ap = ArithmeticProgression(0, 1/3, 1)
    >>> list(ap)
    [0.0, 0.3333333333333333, 0.6666666666666666]
    >>> from fractions import Fraction
    >>> ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    >>> list(ap)
    [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
    >>> from decimal import Decimal
    >>> ap = ArithmeticProgression(0, Decimal('.1'), .3)
    >>> list(ap)
    [Decimal('0'), Decimal('0.1'), Decimal('0.2')]
    >>> ap = ArithmeticProgression(0, Decimal('.2'))
    >>> i_ap = iter(ap)
    >>> next(i_ap)
    Decimal('0')
    >>> next(i_ap)
    Decimal('0.2')

Test of `aritprog_gen`
    >>> ap = aritprog_gen(0, 1, 3)
    >>> list(ap)
    [0, 1, 2]
    >>> ap = aritprog_gen(1, .5, 3)
    >>> list(ap)
    [1.0, 1.5, 2.0, 2.5]
    >>> ap = aritprog_gen(0, 1/3, 1)
    >>> list(ap)
    [0.0, 0.3333333333333333, 0.6666666666666666]
    >>> from fractions import Fraction
    >>> ap = aritprog_gen(0, Fraction(1, 3), 1)
    >>> list(ap)
    [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
    >>> from decimal import Decimal
    >>> ap = aritprog_gen(0, Decimal('.1'), .3)
    >>> list(ap)
    [Decimal('0'), Decimal('0.1'), Decimal('0.2')]
    >>> ap = aritprog_gen(0, Decimal('.2'))
    >>> next(ap)
    Decimal('0')
    >>> next(ap)
    Decimal('0.2')

Test of `aritprog_gen2`
    >>> ap = aritprog_gen2(0, 1, 3)
    >>> list(ap)
    [0, 1, 2]
    >>> ap = aritprog_gen2(1, .5, 3)
    >>> list(ap)
    [1.0, 1.5, 2.0, 2.5]
    >>> ap = aritprog_gen2(0, 1/3, 1)
    >>> list(ap)
    [0.0, 0.3333333333333333, 0.6666666666666666]
    >>> from fractions import Fraction
    >>> ap = aritprog_gen2(0, Fraction(1, 3), 1)
    >>> list(ap)
    [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
    >>> from decimal import Decimal
    >>> ap = aritprog_gen2(0, Decimal('.1'), .3)
    >>> list(ap)
    [Decimal('0'), Decimal('0.1'), Decimal('0.2')]
    >>> ap = aritprog_gen2(0, Decimal('.2'))
    >>> next(ap)
    Decimal('0')
    >>> next(ap)
    Decimal('0.2')
"""
import itertools


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        res = type(self.step)(self.begin)
        forever = self.end is None
        while forever or res < self.end:
            yield res
            res += self.step


def aritprog_gen(begin, step, end=None):
    res = type(step)(begin)
    forever = end is None
    index = 0
    while forever or res < end:
        yield res
        index += 1
        res = begin + step * index


def aritprog_gen2(begin, step, end=None):
    begin = type(step)(begin)
    if end is None:
        res = itertools.count(begin, step)
    else:
        res = itertools.takewhile(lambda n: n < end, itertools.count(begin, step))

    return res
