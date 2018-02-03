"""
Test of `with`
    >>> with LookingGlass() as what:
    ...     print('Alice, kitty and Snowdrop')
    ...     print(what)
    pordwonS dna yttik ,ecilA
    ESREVER
    >>> what
    'REVERSE'
    >>> print('Back to normal')
    Back to normal

Test of invoking
    >>> manager = LookingGlass()
    >>> monster = manager.__enter__()
    >>> monster == 'REVERSE'
    eurT
    >>> monster
    'ESREVER'
    >>> manager.__exit__(None, None, None)
    >>> monster
    'REVERSE'
"""


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'REVERSE'

    def reverse_write(self, text):
        return self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please do not divide by Zero')
            return True

