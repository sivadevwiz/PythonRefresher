"""
1. We can declare classes, in addition to the python provided types
2. From classes, we can instantiate the objects
3. Object is the instance of the class
4. Class is the type of the object
"""


class Car:
    def ride(self):
        print("Vrooooooooooom")


tata = Car()
tata.ride()
print(type(tata))  # <class '__main__.Car'>


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof")


roger = Dog("Roger", 8)
print(type(roger))
print(roger.name)
print(roger.age)
print(roger.bark())
