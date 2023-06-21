# Tuples

""""
1. Tuples are used to create immutable groups of objects
2. Once a Tuple is created, it cannot be modified
3. Items cannot be added/removed like in Lists
4. Uses Parenthesis
"""
first_tuple = ("item1", "item2", "item3")

# index can be used to access the data
print(first_tuple[0])  # item1
print(first_tuple[-2])  # 2nd item from the tuple
print(first_tuple[-1])  # last item of Tuple
print("first_tuple.index('item2').....", first_tuple.index("item2"))

print(len(first_tuple))  # 3

print("item2" in first_tuple)
print("item2 " in first_tuple)
print("item2 ".strip() in first_tuple)

print(first_tuple[1:2])  # ('item2',) - Does not print the last one
print(first_tuple[1:3])  # ('item2', 'item3')

second_tuple = (31, 12, 33)
print(sorted(second_tuple))  # [12, 31, 33] - creates a new sorted list and not a tuple

sorted_items = sorted(second_tuple)

print(type(sorted_items))

third_tuple = second_tuple + (2, 3, 4)
print("third_tuple.........", third_tuple)  # (31, 12, 33, 2, 3, 4)

fourth_tuple = ((1, 2), (2, 3), (4, 5))
print(fourth_tuple)

fifth_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(fifth_tuple[2:6])
