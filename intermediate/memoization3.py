from functools import wraps, lru_cache
from time import perf_counter
import sys


@lru_cache(maxsize = 1000)
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print("recurrsion limit..........", sys.getrecursionlimit())
    # sys.setrecursionlimit(5000)
    start = perf_counter()
    f = fibonacci(129)
    end = perf_counter()

    print(f)
    print(f'Time: {end - start} seconds')