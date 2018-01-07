import time

DEFAULT_FMT = '[elapsed:0.8f]s {name}({args}) -> {result}'


def clock_p(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _res = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_res)
            print(fmt.format(**locals()))
            return _res
        return clocked
    return decorate
