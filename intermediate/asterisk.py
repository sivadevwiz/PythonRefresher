my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
my_list = [7, 8, 9]

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict_b = {'d': 4, 'e': 5, 'f': 6}

tuple_tuple_set = (*my_tuple, *my_set)

print(tuple_tuple_set)  # (1, 2, 3, 4, 5, 6)

set_tuple_set = {*my_tuple, *my_set}
print(set_tuple_set)  # {1, 2, 3, 4, 5, 6}

tuple_list_tuple = (*my_list, *my_tuple)
print(tuple_list_tuple)  # (7, 8, 9, 1, 2, 3)

# list_list_dict = [*list, *dict] # TypeError: Value after * must be an iterable, not type
# print(list_list_dict)

dict_dict = {*my_dict, *my_dict_b}
print(dict_dict) # {'d', 'b', 'c', 'f', 'e', 'a'} # we get only keys
print(type(dict_dict)) # <class 'set'>

dict_dict = {**my_dict, **my_dict_b}
print(dict_dict) # {'d', 'b', 'c', 'f', 'e', 'a'} # we get only keys

# dict_dict = {*my_dict, **my_dict_b} # SyntaxError: invalid syntax
# print(dict_dict)

