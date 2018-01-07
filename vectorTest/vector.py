from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # return 'Vector({}, {})'.format(self.x, self.y)
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        """
        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """
        >>> v1 = Vector(0, 0)
        >>> bool(v1)
        False
        >>> v2 = Vector(1, 1)
        >>> bool(v2)
        True
        """
        return bool(abs(self))

    def __add__(self, other):
        """
        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1+v2
        Vector(4, 5)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        """
        return Vector(self.x * scalar, self.y * scalar)
