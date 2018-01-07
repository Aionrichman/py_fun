def clip(text: str, max_len: 'int > 0'=11) -> str:
    """
    >>> clip('this is an example named clip', 5)
    'this'
    >>> clip('thisis an example named clip', 5)
    'thisis'
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.find(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)

    return text[:end].rstrip()
