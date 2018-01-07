class Average:
    """
    >>> avg = Average()
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12)
    11.0
    >>> avg = Average()
    >>> avg()
    0.0
    """
    def __init__(self):
        self.series = []

    def __call__(self, new_value=0):
        self.series.append(new_value)
        res = sum(self.series)/len(self.series)
        return res


def make_average():
    """
    >>> avg = make_average()
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12)
    11.0
    >>> avg.__code__.co_varnames
    ('new_value', 'res')
    >>> avg.__code__.co_freevars
    ('series',)
    >>> avg.__closure__[0].cell_contents
    [10, 11, 12]
    """
    series = []

    def average(new_value):
        series.append(new_value)
        res = sum(series)/len(series)
        return res

    return average


def make_average_nonlocal():
    """
        >>> avg = make_average_nonlocal()
        >>> avg(10)
        10.0
        >>> avg(11)
        10.5
        >>> avg(12)
        11.0
    """
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        res = total/count
        return res

    return average
