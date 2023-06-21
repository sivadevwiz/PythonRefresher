"""" While loop"""

count = 0

while count <= 10:
    print(count)
    count += 1

"""" for loop"""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)

"""" For loop with range"""

for i in range(1, 6):
    print(i)

"""" For loop with enumerate"""

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, 10):
    print(index, fruit)

"""" For loop with zip"""

fruits = ["apple", "banana", "cherry", "mango"]
colors = ["red", "yellow", "red"]

for fruit, color in zip(fruits, colors):
    print(fruit, color)

# it will take only the least of the two List - here only 3

for index, (fruit, color) in enumerate(zip(fruits, colors)):  # enclosing the rest of the items in () is needed.
    # here (fruit, color)
    print(index, fruit, color)

    """" For loop with dict items"""
fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
print("For loop with dict items")
for fruit, color in fruits.items():
    print(fruit, color)

print("For loop with dict items enumerate")
for index, (fruit, color) in enumerate(fruits.items(), 5):
    print(index, fruit, color)
