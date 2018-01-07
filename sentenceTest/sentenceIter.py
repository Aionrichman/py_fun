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
    >>> it = iter(s)
    >>> for i in range(len(s)):
    ...     print(it.index)
    ...     next(it)
    0
    'The'
    1
    'Time'
    2
    'has'
    3
    'come'
    4
    'the'
    5
    'Walrus'
    6
    'said'
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self
