"""
Lambda functions
1. Tiny functions with no name and are anonymous
2. they will have only one expression as their body
3. defined by the lambda keyword
"""

# here num is the argument and the expression is on the RHS of the colon
lambda num: num * 2

multiply = lambda a, b: a * b

print(multiply(2, 5))

# map(), filter(), reduce()

list_a = [1, 2, 3, 4, 5]


def double(a):
    return a * 2


# result = map(double, list_a)
result = map(lambda num: num * 2, list_a)

print(list(result))

result = filter(lambda num: num % 2 == 0, list_a)

print(list(result))

students= {"name": "John Doe", "grade": 90, "age": 15}

doubled_grades = map(lambda x: x * 2, students.values()) # ['John DoeJohn Doe', 180, 30]

print("doubled_grades..........", list(doubled_grades))

# Reduce

expenses = [('Dinner', 80), ('Movie', 30)]

from functools import reduce

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)
