print(1 + 1)
print(1 + -1)
print(2 - 1)
print(2 * 2)
print(4 / 2)
print(4 % 3)  # Reminder of 4/3
print(4 ** 2)  # 4^2 = 16
print(5 // 2)  # 2 - Divides and rounds down to the nearest whole number

age = 8
age += 8  # 16 -> 8 + 8
print(age)

test = "num "
print(test * 8)  # num num num num num num num num

# print(test / 5) # TypeError: unsupported operand type(s) for /: 'str' and 'int'


# comparison operators

a = 1;
b = 2

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a >= b)
print(a is b)  # 'is' is called identity operator
array = [1, 2, 3]
print(1 in array)  # 'in' is called membership operator

# Boolean operators
cond1 = True
cond2 = False

print(not cond1)  # False
print(cond1 and cond2)  # False
print(cond1 or cond2)  # True

# Or conditional checks
print("0 or 1>>>", 0 or 1)  # 1
print('False or "Hey">>>', False or "Hey")  # Hey
print('True or "Hey">>>', True or "Hey")  # True
print('"hi" or "hey">>>', "hi" or "hey")  # hi
print('"" or "hey">>>', "" or "hey")  # hey
print('"" or False>>>', "" or False)  # False
print('[] or False>>>', [] or False)  # False
print('False or []>>>', False or [])  # []
print('False or "">>>', False or "")  # Empty string
print('[] or "">>>', [] or "")  # Empty string

# and conditional checks
print("\n\nAnd conditional checks")
print("0 and 1>>>", 0 and 1)  # 1
print('False and "Hey">>>', False and "Hey")  # Hey
print('True and "Hey">>>', True and "Hey")  # True
print('"hi" and "hey">>>', "hi" and "hey")  # hi
print('"" and "hey">>>', "" and "hey")  # hey
print('"" and False>>>', "" and False)  # False
print('[] and False>>>', [] and False)  # False
print('False and []>>>', False and [])  # []
print('False and "">>>', False and "")  # Empty string
print('[] and "">>>', [] and "")  # Empty string

print("End of code")


# Bitwise operators
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# shift right operation


# Ternary operators
def is_adult(age):
    if age > 18:
        return True
    else:
        return False


""""
The use of ternary operators will not be like JS.
Care needed
"""


def is_adult_ter(age):
    return True if age > 18 else False


print("is_adult(34)..........", is_adult(34))
print("is_adult_ter(34)..........", is_adult_ter(34))

# Strings
name = "Siva"
name += "Sankaran"

print("name.......{}".format(name))
print(f"name............{name}")

print(f"name in caps........{name.upper()}")
print(f"name in small........{name.lower()}")
print(f"name in Title........{name.title()}")  # Camel case
print(f"name in is lower........{name.islower()}")  # checks if all cases are lower

lowText = "abc"
highText = "ABC"
print(f"lowText in is lower........{lowText.islower()}")  # checks if all cases are lower
print(f"highText in is lower........{highText.islower()}")  # checks if all cases are lower

print(f"lowText in is upper........{lowText.isupper()}")  # checks if all cases are upper
print(f"highText in is upper........{highText.isupper()}")  # checks if all cases are upper

print(f"lowText.isalpha()........{lowText.isalpha()}")  # checks if all are alphabets
print(f"lowText.isalnum()........{lowText.isalnum()}")  # checks if alphanumeric
print("test".isalnum())  # True, because it checks alphabets or number
print(f"lowText.isdecimal()........{lowText.isdecimal()}")  # checks if decimal

print("Siva".startswith("s"))  # False
print("Siva".startswith("S"))  # True

print("Siva".endswith("A"))  # False
print("Siva".endswith("a"))  # True

print("Siva".replace("a", "A"))
print("character".replace("a", "A"))  # chArActer
print("character".replace("a", "A", 1))  # chAracter , because count is only 1

# split - splits the string into list of strings
print("character".split("a"))  # ['ch', 'r', 'cter']
print("character".split("a", 1))  # ['ch', 'racter']
print(type("character".split("a", 1)))  # list

print(" character  ")
print(" character  ".strip())  # removes whitespace from string

# Join - important - it iterates the string to characters within join and adds the string given
list = ['1', '2', '3']
print(" ".join(list))
print(" ".join("test"))
print("123".join("test "))

print("character".find("a"))
print("character".find("a", 3))  # start of substring is mentioned
print("character".find("a", 3, 10))  # start of substring and end is mentioned

print("ch" in "character")

# Escape characters
name = "\"Test\""
print(name)
print("test\nis on")
print("\\")

print(name[3])
print(name[-1])
print(name[-4])
print(name[1:4])
print(name[1:])
print(name[:3])

# Booleans

# check = True

# check = 0 # Value will be False
# check = 3 # Value will be True for any number
check = -10  # Value will be True even for negative number

if check:
    print("Done")
else:
    print("Not done")

done = True

print(type(done) == bool)

cond1 = True
cond2 = False

print(any([cond1, cond2]))  # To be given as a list
print(all([cond1, cond2]))  # To be given as a list
