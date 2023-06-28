# for integer - immutable type

org = 5
cpy = org  # here it only copies the reference
cpy = 6  # here new variable is created
# that's why it prints different values
print(org)
print(cpy)

# for list - mutable type

org = [1, 2, 3]
cpy = org  # here it only copies the reference
cpy[0] = -10  # here it changes in both the places
print(org)  # [-10, 2, 3]
print(cpy)  # [-10, 2, 3]

"""
Shallow copy - Only to one level; for nested child objects only reference is copied
Deep copy - Full independent copy
"""

import copy

org = [1, 2, 3, 4, 5]
cpy = org.copy()
# cpy = copy.copy(org) # another way of copy
cpy[0] = 6
print(org)  # [1, 2, 3, 4, 5]
print(cpy)  # [6, 2, 3, 4, 5]

# Example 2 - shallow copy

org = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
cpy = org.copy()
cpy[0][0] = 6
print(org)  # [[6, 2, 3, 4, 5], [6, 7, 8, 9]]
print(cpy)  # [[6, 2, 3, 4, 5], [6, 7, 8, 9]]

# Example 3 - Deep copy

org = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][0] = 6
print(org)  # [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
print(cpy)  # [[6, 2, 3, 4, 5], [6, 7, 8, 9]]

"""
Class examples
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Siva', 34)
p2 = p1
p2.age = 35

print(p1.age)
print(p2.age)

p1 = Person('Siva', 34)
p2 = copy.copy(p1)
p2.age = 35

print(p1.age)
print(p2.age)

# Shallow copy
p1 = Person('Siva', 34)
p2 = Person('Mini', 30)
# print("class Shallow copy")
# company = Company(p1, p2)
# company_clone = copy.copy(company)  # shallow copies and takes only reference
# company_clone.boss.age = 37
#
# print(company_clone.boss.age)  # 37
# print(company.boss.age)  # 37

# Deep copy
print("class deep copy")
company = Company(p1, p2)
company_clone = copy.deepcopy(company)  # shallow copies and takes only reference
company_clone.boss.age = 37

print(company_clone.boss.age)  # 37
print(company.boss.age)  # 34
