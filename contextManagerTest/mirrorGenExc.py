"""
Test of `with`
    >>> with looking_glass() as what:
    ...     print('Alice, kitty and Snowdrop')
    ...     print(what)
    pordwonS dna yttik ,ecilA
    ESREVER
    >>> what
    'REVERSE'
    >>> print('Back to normal')
    Back to normal

Test of invoking
    >>> manager = looking_glass()
    >>> monster = manager.__enter__()
    >>> monster == 'REVERSE'
    eurT
    >>> monster
    'ESREVER'
    >>> manager.__exit__(None, None, None)
    False
    >>> monster
    'REVERSE'
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        return original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'REVERSE'
    except ZeroDivisionError:
        msg = 'Please do not divide by Zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
