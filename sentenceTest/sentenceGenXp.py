""""
    >>> s = Sentence('"The Time has come," the Walrus said')
    >>> s
    Sentence('"The Time ha...e Walrus said')
    >>> for word in s:
    ...     print(word)
    The
    Time
    has
    come
    the
    Walrus
    said
    >>> list(s)
    ['The', 'Time', 'has', 'come', 'the', 'Walrus', 'said']
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
