"""
Inheritance - process by which one class takes attributes and methods of another class
The newly formed class is called the child class and the original class is called the parent class
"""


# parent or base class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working....")


# For inheritance, we add the base class as parameter to the child class
# inherits all the attributes and functions from Employee class
class SoftwareEngineer(Employee):
    pass


class Designer(Employee):
    pass


# se = SoftwareEngineer() # TypeError: Employee.__init__() missing 2 required positional arguments: 'name' and 'age'
# though the __init__ is not defined within the SoftwareEngineer class, it inherits the properties of the base class and
# hence we need to provide the arguments

se = SoftwareEngineer("max", 20)
print(se.name, se.age)
se.work()

# similarly creating a designer instance
de = Designer("phil", 25)
print(de.name, de.age)
de.work()
