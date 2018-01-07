import time
import functools

from clockdecoTest.clockdeco import clock
from clockdecoTest.clockdeco_param import clock_p


@clock_p('{name}({args}): dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print('*'*40, 'Calling snooze(.123)')
    for i in range(3):
        snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6!=', factorial(6))
    print('*' * 40, 'Calling fibonacci(6)')
    print(fibonacci(30))
