"""
    >>> coro_avg = averager()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
    >>> coro_avg.send('spam')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +=: 'float' and 'str'
    >>> coro_avg.send(60)
    Traceback (most recent call last):
        ...
    StopIteration
"""

from coroutineTest.coroutil import coroutine


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
