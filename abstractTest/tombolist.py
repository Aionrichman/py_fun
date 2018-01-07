"""
    >>> issubclass(TomboList, Tombola)
    True
    >>> t = TomboList(range(100))
    >>> isinstance(t, Tombola)
    True
    >>> TomboList.__mro__
    (<class 'tombolist.TomboList'>, <class 'list'>, <class 'object'>)
"""
from random import randrange
from abstractTest.tombola import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomblList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

