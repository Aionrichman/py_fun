from array import array
from random import random
from time import perf_counter as pc


def write_file(float_i, file_path):
    fp = open(file_path, 'wb')
    float_i.tofile(fp)
    fp.close()


def get_file(file_path):
    floats_o = array('d')
    fp = open(file_path, 'rb')
    floats_o.fromfile(fp, 10**7)
    fp.close()

    return floats_o


def div_cost(float_i):
    t0 = pc()
    for float_s in float_i:
        float_s /= 3
    res = pc() - t0

    return res


if __name__ == '__main__':
    floats = array('d', (random() for i in range(10 ** 7)))
    t_cost = div_cost(floats)
    print(t_cost)

    path = 'C:\\Users\\aion\\Desktop\\py_fun\\floats.bin'
    write_file(floats, path)
    floats2 = get_file(path)
    print('{0}\n{1}'.format(floats[-3:], floats2[-3:]))
    if floats == floats2:
        print('Success')
    else:
        print('Fail')


