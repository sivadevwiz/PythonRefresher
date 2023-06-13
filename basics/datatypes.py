name = "Shiva"
print(type(name))  # <class 'str'>
print(type(name) == str)  # True
print(type(name == str))  # <class 'bool'>, because comparison is within type

print(isinstance(name, str))  # True

age = 2

print(isinstance(age, int))  # True
print(isinstance(age, float))  # False, because no decimal point

# Type casting examples
new_age = float(2)  # Converting integer to float
print(isinstance(new_age, float))  # True, variable is created as float using the class constructor.

new_age = float("34")  # works for string too
print("New age - string converted to float>>>", new_age)
print(isinstance(new_age, float))  # True, variable is created as float using the class constructor.

new_age = float("test")  # Will throw error
print("New age - string converted to float>>>", new_age)
print(isinstance(new_age, float))  # ValueError: could not convert string to float: 'test'

