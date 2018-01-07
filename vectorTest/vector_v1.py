"""
A vector class
    >>> Vector([3.1, 4.1])
    Vector([3.1, 4.1])
    >>> Vector([3, 4, 5])
    Vector([3.0, 4.0, 5.0])
    >>> Vector(range(10))
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

Test of `__bytes__` and `frombytes()`
    >>> v1 = Vector([3, 4, 5])
    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone == v1
    True
    >>> v1 == (3, 4, 5)
    False
    >>> v1 != (3, 4, 5)
    True

Test of slicing
    >>> len(v1)
    3
    >>> v1[0], v1[-1]
    (3.0, 5.0)
    >>> v7 = Vector(range(7))
    >>> v7[1:4]
    Vector([1.0, 2.0, 3.0])
    >>> v7[-1:]
    Vector([6.0])
    >>> v7[1,2]
    Traceback (most recent call last):
        ...
    TypeError: Vector indices must be integers

Test of operator
    >>> -v1
    Vector([-3.0, -4.0, -5.0])
    >>> +v1
    Vector([3.0, 4.0, 5.0])
    >>> v1 + v7
    Vector([3.0, 5.0, 7.0, 3.0, 4.0, ...])
    >>> v1 + (10, 20, 30)
    Vector([13.0, 24.0, 35.0])
    >>> (10, 20, 30) + v1
    Vector([13.0, 24.0, 35.0])
    >>> v1 + 1
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
    >>> v1 + 'ABC'
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'Vector' and 'str'

Test of mul
    >>> 14 * v1
    Vector([42.0, 56.0, 70.0])
    >>> v1 * True
    Vector([3.0, 4.0, 5.0])
    >>> from fractions import Fraction
    >>> v1 * Fraction(1, 3)
    Vector([1.0, 1.3333333333333333, 1.6666666666666665])
    >>> va = Vector([1, 2, 3])
    >>> vz = Vector([5, 6, 7])
    >>> va @ vz
    38.0
    >>> [10, 20, 30] @ vz
    380.0
    >>> [10, 20, 30, 40] @ vz
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for @: 'Vector' and 'list'

Test of attribute
    >>> v5 = Vector(range(5))
    >>> v5.z
    2.0
    >>> v5.x = 10
    Traceback (most recent call last):
        ...
    AttributeError: readonly attribute 'x'
    >>> v5.a = 10
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute 'a' to 'z' in 'Vector'
    >>> v5.H = 10
    >>> v5.H
    10

Test of hashing
    >>> v2 = Vector([3, 4])
    >>> v3 = Vector([3, 4, 5])
    >>> v6 = Vector(range(6))
    >>> hash(v2), hash(v3), hash(v6)
    (7, 2, 1)

Test of format
    >>> format(Vector([1, 1]), 'h')
    '<1.4142135623730951,0.7853981633974483>'
    >>> format(Vector([1, 1, 1]), 'h')
    '<1.7320508075688772,0.9553166181245093,0.7853981633974483>'
    >>> format(Vector([2, 2, 2]), '.3eh')
    '<3.464e+00,9.553e-01,7.854e-01>'
    >>> format(Vector([0, 0, 0]), '.5fh')
    '<0.00000,0.00000,0.00000>'
    >>> format(Vector([-1, -1, -1, -1]), '.3eh')
    '<2.000e+00,2.094e+00,2.186e+00,3.927e+00>'
    >>> v9 = Vector(range(9))
    >>> format(v9, '.3e*')
    '(0.000e+00,1.000e+00,2.000e+00,3.000e+00,4.000e+00,5.000e+00,6.000e+00,7.000e+00,8.000e+00)'
    >>> format(v9, '.5f')
    '(0.00000,1.00000,2.00000,3.00000, ...)'
    >>> format(v9, '.3eh*')
    '<1.428e+01,1.571e+00,1.501e+00,1.430e+00,1.356e+00,1.276e+00,1.182e+00,1.057e+00,8.520e-01>'
    >>> format(v9, '.5fh')
    '<14.28286,1.57080,1.50072,1.42996, ...>'
"""

from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
    type_code = 'd'
    default_len = 4
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        class_name = type(self).__name__
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return '{}({})'.format(class_name, components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.type_code)]) + bytes(self._components)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented
        # if len(self) != len(other):
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            return Vector(x + y for x, y in itertools.zip_longest(self, other, fillvalue=0.0))
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector(x * other for x in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        if len(self) == len(other):
            return sum(x * y for x, y in zip(self, other))
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    # 牛逼啊
    def __format__(self, fmt_spec):
        if fmt_spec.endswith('*'):
            fmt_spec = fmt_spec[:-1]
            short_flag = ''
        elif len(self) > self.default_len:
            short_flag = ', ...'
        else:
            short_flag = ''

        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'

        if short_flag:
            components = [format(c, fmt_spec) for c in list(coords)[:self.default_len]]
        else:
            components = [format(c, fmt_spec) for c in coords]

        return outer_fmt.format(','.join(components) + short_flag)

    @classmethod
    def frombytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(memv)
