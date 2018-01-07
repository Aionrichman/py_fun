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
        self.words = RE_WORD.findall(text)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return
