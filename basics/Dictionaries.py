""""
1. Dictionaries - key value pairs
2. uses curly braces
"""

dog = {"name": "Roger", "age": 8, "address": {"street": "street1", "code": "001"}}

print(dog)

# print(dog[1]) # KeyError: 1

# print(dog("name")) # TypeError: 'dict' object is not callable

print(dog["name"])  # Roger - Always use the square brackets

print(dog["address"]["code"])

dog["name"] = "Timmy"

print(dog["name"])  # Timmy

dog["address"]["code"] = "007"
print(dog["address"]["code"])

# use get() to get the value
print(dog.get("name"))  # Timmy

# use nested get() to get the value of code
print(dog.get("address").get("code"))  # 007

print('"name" in dog..........', "name" in dog)  # True
print('"color" in dog..........', "color" in dog)  # False

# Keys
print(dog.keys())  # dict_keys(['name', 'age', 'address'])

keys = dog.keys()
print(type(keys))  # <class 'dict_keys'>

key_list = list(keys)
print(key_list)  # ['name', 'age', 'address']
print(type(key_list))  # <class 'list'>

# Values
print(dog.values())  # dict_values(['Timmy', 8, {'street': 'street1', 'code': '007'}])
print(type(dog.values()))  # <class 'dict_values'>
dog_list = list(dog.values())
print("dog_list.....", dog_list)
print("type(dog_list).....", type(dog_list))  # <class 'list'>

# items

print("dog.items()...........",
      dog.items())  # dict_items([('name', 'Timmy'), ('age', 8), ('address', {'street': 'street1', 'code': '007'})])
print(type(dog.items()))  # <class 'dict_items'>

# len
print("len(dog).........", len(dog))  # will give only 3 based on hierarchy of nesting

print(dog.get("color"))  # None
print(dog.get("color", "Black"))  # Black - default value
# print(dog.get("color", default="Brown"))  # Brown - default value  mentioned explicitly with keyword
# Default values cannot be given in the object notation

print(dog.pop("name"))
print(dog)

# Copy dictionary
dog_copy = dog.copy()
print("dog_copy..........", dog_copy)

# Adding items

dog["food"] = "treat"
print("dog........", dog)

# Removing items

del dog["food"]

print("dog........", dog)

# del dog # Deletes the dog dict itself
# print("Deleted dog")


print(dog.popitem())  # Removes last key in the dictionary. no key can be specified.
print(dog)

# dictionaries don't allow duplicates and just take the 2nd value of the same key value pair
cat = {"name": "kitty", "age": 5, "age": 9}
print("cat..........", cat)

