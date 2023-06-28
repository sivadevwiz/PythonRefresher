""""
Sets - unordered, mutable, no duplicates
1. Sets are like tuples but not ordered and mutable (value can be changed)
2. They work like dictionaries but got no keys
3. There's an immutable set version - Frozen set
4. uses Curly braces
"""

set1 = {'Bond', 'Alec'}
set2 = {"Bond", "Goldfinger", "Natalya"}

myset = set([1, 2, 3])
print(myset)

myset = set("Hello")
print(myset)  # {'o', 'e', 'l', 'H'} - will be random and only only "l" means that duplicates will not be added

intersect = set1 & set2
print(intersect)  # {'Bond'}

intersect2 = set1 and set2
print(intersect2)  # {'Bond', 'Natalya', 'Goldfinger'} - gives the set2 always in random order

union = set1 | set2  # {'Bond', 'Goldfinger', 'Alec', 'Natalya'}

print(union)

union2 = set1 or set2  # {'Bond', 'Alec'} - gives first set; if first set is empty will return the other

print(union2)

# Difference

diff = set1 - set2
print("diff.......", diff)

diff2 = set2 - set1
print("diff2.......", diff2)

diff2 = set2.difference(set1)
print("diff2.......", diff2)

diff2 = set2.symmetric_difference(set1)
print("symmetric_difference.......", diff2)

# Check superset and subset
print(set1 < set2)

set3 = {1, 2, 3}
set4 = {1}
print(set3 > set4)
print(set3 < set4)

list_set3 = list(set3)
print(list_set3)

# Check item present in set
print(1 in set3)

# Set cannot have duplicate items
set5 = {1, 1, 2, 2, 3, 3, 3}
print(set5)  # {1, 2, 3}

# set6 = {{1, 2}, {2, 3}, [11, 2, 3], (2, 3, 4)} # TypeError: unhashable type: 'set'
# set6 = {{1, 2}, {2, 4}} # TypeError: unhashable type: 'set'
# set6 = {[1,2,3], 2,3} # TypeError: unhashable type: 'list'
set6 = {(2, 3), (1, 2)}  # {(2, 3), (1, 2)}

print(set6)
print(type(set6))  # <class 'set'>

# empty set will be always considered as dict
set7 = {}
print(type(set7))  # <class 'dict'>

set7 = set()
print(type(set7))  # <class 'set'>

# adding items to set

set8 = {1, 2, 3}
set8.add(4)
print(set8)

# set8.add({5,6,7}) # Doesn't work
# print(set8)

# set8.add(4, 5, 6) # multiple items cannot be added
# print(set8)

set9 = set()

set9.add(1)
set9.add(2)
set9.add(3)

print(set9)

set9.remove(1)
set9.discard(2)
set9.discard(4)  # will not throw error
print(set9)

set9.clear()
print(set9)

set10 = {111, 12, 3, 4, 5, 6}
print(set10.pop())
print(set10)

for i in set10:
    print(i)

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 6, 7, 8, 9}

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 6, 7, 8, 9}

setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 6, 7, 8, 9}

setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 6, 7, 8, 9}

setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setC = {10, 11}

print(setA.issubset(setB))
print(setB.issubset(setA))
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

fSet = frozenset([1, 2, 3, 4])
# fSet = frozenset[1, 2, 3, 4]
print(fSet)
# .add and .remove will cause error on frozen SET. however union and intersections will work
