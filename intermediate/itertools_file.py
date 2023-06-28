# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count,\
    cycle, repeat
import operator
import time

# a = [1, 2]
# b = [3, 4]

# prod = product(a, b)
# print(list(prod))
#
# c = [1, 2]
# d = [3]
#
# print(list(product(c, d)))
# print(list(product(c, d, repeat=2)))

a = [1, 2, 3]

# perm = permutations(a)
# print(list(perm))
#
# perm = permutations(a, 2)
# print(list(perm))
#
# perm = permutations(a, 4)
# print(list(perm)) # []

# comb = combinations(a, 2)
# comb = combinations(a, 2)
# print(list(comb))
#
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))

# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))
#
# acc = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))
#
# b = [1, 2, 5, 3, 4]
# acc = accumulate(b, func=max)
# print(b)
# print(list(acc))
#
#
# def smaller_than_3(x):
#     return x < 3
#
#
# group_obj = groupby(a, key=smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value))
#
# # Example with lambda
#
# group_obj_2 = groupby(a, key=lambda x: x < 3)
# for key, value in group_obj_2:
#     print(key, list(value))
#
# persons = [{'name': 'X', 'age': 25},
#            {'name': 'Y', 'age': 26},
#            {'name': 'Z', 'age': 27},
#            {'name': 'A', 'age': 25}]
#
#
# group_persons = groupby(persons, key= lambda x: x['age'])
# for key,value in group_persons:
#     print(key, list(value))


# for i in count(10):
#     print(i)
#     if i == 15:
#         break
#

# Cycle

a = [1,2,3]

# for i in cycle(a):
#     print(i)
#     time.sleep(1)

# for i in repeat(a):
#     print(i)
#     time.sleep(1)

# for i in repeat(2):
#     print(i)
#     time.sleep(1)
#
for i in repeat(2,4): # arg 1: item to repeat; arg 2 - number of repeat
    print(i)
    time.sleep(1)


