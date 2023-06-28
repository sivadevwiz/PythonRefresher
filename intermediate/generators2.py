import sys
def firstn(num):
    nums = []
    n = 0
    while n < num:
        nums.append(n)
        n += 1
    return nums


print(firstn(10))
print(sum(firstn(10)))


def firstn_generator(num):
    n = 0
    while n < num:
        yield n
        n += 1


n = firstn_generator(10)

print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

print(sum(firstn_generator(10)))



print(sys.getsizeof(firstn(10)))
print(sys.getsizeof(firstn_generator(10)))
