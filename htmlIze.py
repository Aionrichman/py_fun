import html
import numbers
from collections import abc
from functools import singledispatch


@singledispatch
def htmlize(obj):
    """
    >>> htmlize({1, 2, 3})
    '<pre>{1, 2, 3}</pre>'
    >>> htmlize(abs)
    '<pre>&lt;built-in function abs&gt;</pre>'
    >>> htmlize('Heimlich & Co, \\n - a game')
    '<p>Heimlich &amp; Co, <br>\\n - a game</p>'
    >>> htmlize(42)
    '<pre>42(0x2a)</pre>'
    >>> print(htmlize(['alpha', 66, {3, 2, 1}]))
    <ul>
    <li><p>alpha</p></li>
    <li><pre>66(0x42)</pre></li>
    <li><pre>{1, 2, 3}</pre></li>
    </ul>
    """
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0}(0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
