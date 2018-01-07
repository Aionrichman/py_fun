import bisect as bs
import sys
import random


def demo():
    haystack = [random.randint(0, 100) for i in range(30)]
    haystack.sort()
    needles = [random.randint(0, 100) for j in range(10)]
    row_format = '{0:2d} @ {1:2d}   {2}{0:<2d}'

    if sys.argv[-1] == 'left':
        bisect_fn = bs.bisect_left
    else:
        bisect_fn = bs.bisect

    print('DEMO', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in haystack))
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)
        offset = position * '  |'
        print(row_format.format(needle, position, offset))


def create_seq(size):
    res = []
    for i in range(size):
        new_item = random.randint(0, 100)
        bs.insort(res, new_item)
        print('%2d ->' % new_item, res)
    return res


def get_grade(point_i):
    breakpoints = range(60, 100, 10)
    grades = 'EDCBA'

    position = bs.bisect(breakpoints, point_i)
    return grades[position]


if __name__ == '__main__':
    demo()
    print('----------------------------------------')
    points = create_seq(10)
    points[10:] = [60, 70, 80, 90, 100]
    print('----------------------------------------')
    for point in points:
        grade = get_grade(point)
        print(point, grade)
