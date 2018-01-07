def tag(name, *content, cls=None, **attrs):
    """
    >>> tag('br')
    '<br />'
    >>> tag('p', 'hello')
    '<p>hello</p>'
    >>> tag('p', 'hello', 'world')
    '<p>hello</p>\\n<p>world</p>'
    >>> tag('p', 'hello', id=33)
    '<p id="33">hello</p>'
    >>> tag('p', 'hello', 'world', cls='sidebar')
    '<p class="sidebar">hello</p>\\n<p class="sidebar">world</p>'
    >>> tag(content='testing', name='img')
    '<img content="testing" />'
    >>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    >>> tag(**my_tag)
    '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' {}="{}"'.format(attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        html_str = '\n'.join('<{0}{1}>{2}</{0}>'.format(name, attr_str, c) for c in content)
    else:
        html_str = '<{}{} />'.format(name, attr_str)

    return html_str
