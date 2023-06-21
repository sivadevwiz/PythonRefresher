""""
1. Sets are like tuples but not ordered and mutable (value can be changed)
2. They work like dictionaries but got no keys
3. There's an immutable set version - Frozen set
4. uses Curly braces
"""

set1 = {'Bond', 'Alec'}
set2 = {"Bond", "Goldfinger", "Natalya"}

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
print(type(set7))

# adding items to set

set8 = {1, 2, 3}
set8.add(4)
print(set8)


# set8.add({5,6,7}) # Doesn't work
# print(set8)

# set8.add(4, 5, 6) # multiple items cannot be added
# print(set8)
