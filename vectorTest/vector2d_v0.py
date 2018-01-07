"""
    >>> v1 = Vector2d(3, 4)
    >>> print(v1.x, v1.y)
    3.0 4.0
    >>> x, y = v1
    >>> x
    3.0
    >>> x, y
    (3.0, 4.0)
    >>> v1
    Vector2d(3.0, 4.0)
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> octets = bytes(v1)
    >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> len(octets)
    17
    >>> v1.type_code = 'f'
    >>> dump = bytes(v1)
    >>> dump
    b'f\\x00\\x00@@\\x00\\x00\\x80@'
    >>> len(dump)
    9
    >>> Vector2d.type_code
    'd'
    >>> sv = ShortVector(1/11, 1/27)
    >>> len(bytes(sv))
    9
    >>> abs(v1)
    5.0
    >>> bool(v1), bool(Vector2d(0, 0))
    (True, False)
    >>> v2 = Vector2d.frombytes(bytes(v1))
    >>> v2
    Vector2d(3.0, 4.0)
    >>> format(v1)
    '(3.0, 4.0)'
    >>> format(v1, '.2f')
    '(3.00, 4.00)'
    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'
    >>> v3 = Vector2d(1, 1)
    >>> format(v3, 'p')
    '<1.4142135623730951, 0.7853981633974483>'
    >>> format(v3, '.3ep')
    '<1.414e+00, 7.854e-01>'
    >>> format(v3, '.5fp')
    '<1.41421, 0.78540>'
    >>> v4 = Vector2d(3.1, 4.2)
    >>> hash(v1), hash(v4)
    (7, 384307168202284039)
    >>> set([v1, v4])
    {Vector2d(3.1, 4.2), Vector2d(3.0, 4.0)}
"""

from array import array
import math


class Vector2d:
    # __slots__ = ('__x', '__y', '__weakref__')
    type_code = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.type_code)])) + (bytes(array(self.type_code, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    @classmethod
    def frombytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)


class ShortVector(Vector2d):
    type_code = 'f'
