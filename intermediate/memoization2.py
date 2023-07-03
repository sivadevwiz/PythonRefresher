import time

# original function
# def expensive_func(n):
#     print("Computing {}.......".format(n))
#     time.sleep(1)
#     result = n * n
#     return result

memz_cache = {}


# memoized function
def expensive_func(n):
    print("Computing {}.......".format(n))
    if n in memz_cache:
        return memz_cache[n]
    time.sleep(1)
    result = n * n
    memz_cache[n] = result
    return result


result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)


