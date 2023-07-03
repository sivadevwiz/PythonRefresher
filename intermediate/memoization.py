from functools import wraps
from time import perf_counter
import sys


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@memoize
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# another implementation without recursion
def new_fibonacci(n):
    fibo = []
    for i in range(n + 1):
        if i < 2:
            fibo.append(i)
        else:
            count = fibo[-1] + fibo[-2]
            fibo.append(count)
        print("{}........ {}".format(i, fibo))

    return fibo, fibo[-1]


if __name__ == '__main__':
    print("recurrsion limit..........", sys.getrecursionlimit())
    sys.setrecursionlimit(5000)
    start = perf_counter()
    f = fibonacci(500)
    end = perf_counter()

    # print(fibonacci(5))
    print(new_fibonacci(500))
    print(f)
    print(f'Time: {end - start} seconds')
