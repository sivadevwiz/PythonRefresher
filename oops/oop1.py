"""
Why we need classes?
Classes are used for more complex data structures

Classes are blueprint of how something is to be defined
"""


# in this example

# Creating a Class - blueprint
# create an instance (object)
# class vs instance (object)
# instance attributes: defined in __init__(self)
# class attributes

# class
class SoftwareEngineer:
    # class attribute
    alias = "Dev Wizard"

    def __init__(self, name, age, level, pay):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.pay = pay


# instance
se1 = SoftwareEngineer("Siva", 34, "TL", 40)
print(se1.name,
      se1.age)  # here the name and age refer to the self.name and self.age which are the instance attributes and
# not the name and age which are the parameters
print(se1.alias)
print(SoftwareEngineer.alias)
