def countdown(num):
    print("starting....")
    while num > 0:
        yield num
        num -= 1
    print("end...")

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd)) # StopIteration
