list_one = [1, 2, 3]
list_two = ["one", 2, "three", True]

print(list_one)  # [1, 2, 3]
print(list_two)  # ['one', 2, 'three', True]

print("three" in list_two)  # True
print(False in list_two)  # False
print(True in list_two)  # True

print(list_two[2])  # three

list_two[2] = "two"  # changes the value

print(list_two[2])  # two - value changed

print(list_two[:])  # ['one', 2, 'two', True]

print(list_two[:3])  # ['one', 2, 'two']
print(len(list_two))  # 4

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
# data types should be same in the List
list_three = [1, 24, 13, 54, 25]
print(list_three.sort())  # None

list_three.sort()
print(list_three)  # [1, 13, 24, 25, 54]

list_four = ["d", "a", "z", "s"]
list_four.sort()
print(list_four)  # ['a', 'd', 's', 'z']

character_names = ['James', "Jackie", "JAckie", "jackie", 'Natal', 'Boris', 'Xenia',
                   'Alec']
character_names.sort()
print(character_names)  # ['Alec', 'Boris', 'JAckie', 'Jackie', 'James', 'Natal', 'Xenia', 'jackie']

character_names.sort(key=str.lower) # fixes the issue of sorting
print(character_names) # ['Alec', 'Boris', 'JAckie', 'Jackie', 'jackie', 'James', 'Natal', 'Xenia']

#copying the items
list_four = ["d", "a", "z", "s"]
list_five = list_four[:]
list_five.sort()
print(list_four)
print(list_five)

# Global function - creates new List instead of modifying the original list
print(sorted(list_four))
print(sorted(list_four, key=str.lower))
print(list_four)
