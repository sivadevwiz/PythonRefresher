"""
Inheritance - part 2
Extends
"""


# parent or base class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working....")


class SoftwareEngineer(Employee):
    pass


class Designer(Employee):
    pass


se = SoftwareEngineer("max", 20)
print(se.name, se.age)
se.work()

# similarly creating a designer instance
de = Designer("phil", 25)
print(de.name, de.age)
de.work()
