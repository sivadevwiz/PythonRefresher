"""
List - Ordered, Mutable, allows duplicate items
"""

list_one = [1, 2, 3]
list_two = ["one", 2, "three", True]  # Lists can have different data types

print(list_one)  # [1, 2, 3]
print(list_two)  # ['one', 2, 'three', True]

print("three" in list_two)  # True
print(False in list_two)  # False
print(True in list_two)  # True

print(list_two[2])  # three - reference using index

list_two[2] = "two"  # changes the value

print(list_two[2])  # two - value changed

print(list_two[:])  # ['one', 2, 'two', True]

print(list_two[:3])  # ['one', 2, 'two']
print(len(list_two))  # 4

print("list_two[::1]", list_two[::1])
print("list_two[::2]", list_two[::2])  # prints every 2nd item - step 2
print("list_two[1::2]", list_two[1::2])

list_two.append(5)
print(list_two)  # ['one', 2, 'two', True, 5]

list_two.extend([6, False, "new"])
# in extend the value can be passed as List only
print(list_two)  # ['one', 2, 'two', True, 5, 6, False, 'new']

# it should be passed as List
list_two += ["Newer", True]
print(list_two)  # ['one', 2, 'two', True, 5, 6, False, 'new', 'Newer', True]

# if not passed as List, it adds each characters as separate entry
list_two += "123"
print(list_two)  # ['one', 2, 'two', True, 5, 6, False, 'new', 'Newer', True, '1', '2', '3']

list_two.remove('1')

print(list_two)  # ['one', 2, 'two', True, 5, 6, False, 'new', 'Newer', True, '2', '3']

# list_two.remove(['2', '3'])
# print(list_two) # ValueError: list.remove(x): x not in list


print(list_two.pop())  # pops '3' which is the last item
print(list_two)  # ['one', 2, 'two', True, 5, 6, False, 'new', 'Newer', True, '2']

# insert is used to add a value in the specific index
list_one.insert(1, "Test")
print(list_one)  # [1, 'Test', 2, 3]

# list_one.insert(4) # TypeError: insert expected 2 arguments, got 1

list_one[3:3] = ["4", "5"]
print(list_one)

list_one[1:5] = ["6", "7"]  # it slices the index on higher range
print(list_one)

# Sort
# ⚠ IMPORTANT! data types should be same in the List
list_three = [1, 24, 13, 54, 25]
print("list_three.sort().........", list_three.sort())  # None as it's only a statement and not an expression

list_three.sort()
print(list_three)  # [1, 13, 24, 25, 54]

list_four = ["d", "a", "z", "s"]
list_four.sort()
print(list_four)  # ['a', 'd', 's', 'z']

character_names = ['James', "Jackie", "JAckie", "jackie", 'Natal', 'Boris', 'Xenia',
                   'Alec']
character_names.sort()
print(character_names)  # ['Alec', 'Boris', 'JAckie', 'Jackie', 'James', 'Natal', 'Xenia', 'jackie']

character_names.sort(key=str.lower)  # fixes the issue of sorting - "jackie" is included in the order
print("key=str.lower....",
      character_names)  # ['Alec', 'Boris', 'JAckie', 'Jackie', 'jackie', 'James', 'Natal', 'Xenia']]

character_names.sort(key=str.upper)  # Same result as above
print("key=str.upper....",
      character_names)  # ['Alec', 'Boris', 'JAckie', 'Jackie', 'jackie', 'James', 'Natal', 'Xenia']

# copying the items
list_a = [1, 2, 3]
list_b = list_a  # will have the same reference

list_a.append(4)
print("list_a", list_a)
print("list_b", list_b)

list_c = [1, 2, 3]
# list_d = list_c.copy() # option 1
# list_d = list_c[:] # option 2
list_d = list(list_c)  # option 3
list_c.append(4)
print("list_c", list_c)  # [1, 2, 3, 4]
print("list_d", list_d)  # [1, 2, 3]

list_four = ["d", "a", "z", "s"]
list_five = list_four[:]
# list_four.sort()
list_five.sort()
print("original list........", list_four)
print("sorted list........", list_five)

# Global function "sorted" - creates new List instead of modifying the original list
print(sorted(list_four))
print(sorted(list_four, key=str.lower))
print(list_four)

character_new = ['James', "Jackie", "JAckie", "jackie", 'Natal', 'James', 'Boris', 'Xenia',
                 'Alec']

print(sorted(character_new))
print(sorted(character_new, key=str.lower))
print(character_new)
print('character_new.index("Jackie").....', character_new.index("Jackie"))  # 1
print('character_new.index("Jackie").....', character_new.index("James"))  # 0 - First index of occurrence

# List concatenation
list_six = list_two + list_four + [100, 101, 102]
print("'list_six'..........", list_six)

list_seven = [1, 2, 3, 4, 5]

list_eight = [1, 2, 3]

list_eight = list_seven + list_eight

print("list_eight........", list_eight)  # [1, 2, 3, 4, 5, 1, 2, 3]

# Only concat will work.
# list_nine = list_seven - list_eight # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(list_nine)

# clear list

list_nine = [1, 2, 3, 4, 5]

print("list_nine", list_nine)
list_nine.clear()
print("list_nine", list_nine)

# remove

list_ten = [1, 2, 23, 4, 5, 5, 6]

list_ten.remove(5)

print("list_ten", list_ten)  # removes the first instance

# reverse

list_11 = [1, 2, 3, 4, 5]

a = list_11[::-1]  # reverses the list

print(a)

list_11.reverse()

print("list_11", list_11)

# list arithmetic

list_12 = [0] * 5

print("list_12", list_12)

# List comprehension

list_13 = [1, 2, 3, 4, 5, 6]
list_14 = [i * i for i in list_13]
print("list_14.......", list_14)
