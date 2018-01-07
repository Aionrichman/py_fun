import sys
import re

WORD_RE = re.compile(r'\w+')


def get_word_index(file_name):
    index = {}

    with open(file_name, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word_re = match.group()
                column_no = match.start()+1
                location_re = (line_no, column_no)
                index.setdefault(word_re, []).append(location_re)
                # occurrences = index.get(word_re, [])
                # occurrences.append(location_re)
                # index[word_re] = occurrences
                # -------------------------------------
                #  if word_re not in index:
                #     index[word_re] = []
                # index[word_re].append(location_re)

    fp.close()
    return index


def get_word_index_default(file_name):
    from collections import defaultdict
    index = defaultdict(list)

    with open(file_name, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word_re = match.group()
                column_no = match.start()+1
                location_re = (line_no, column_no)
                index[word_re].append(location_re)

    fp.close()
    return index


if __name__ == '__main__':
    file = sys.argv[1]
    word_index = get_word_index_default(file)
    print('find {} words'.format(len(word_index)))
    for word in sorted(word_index, key=str.upper):
        location = word_index[word]
        print('{0:10s}{1:4d}{2}'.format(word, len(location), location))
