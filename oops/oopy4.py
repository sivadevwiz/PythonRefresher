"""
Inheritance - part 2
Extends
"""

"""
Same function name in child class - overrides
new function added in child class - extends
"""

"""
inheritance: ChildClass(BaseClass)
inherit, extend and override - attributes & function
super().__init__() - when overriding the init in child class, we need to add super()
"""

# parent or base class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working....")


class SoftwareEngineer(Employee): # inheritance
    def __init__(self, name, age, salary, level):  # overrides
        super().__init__(name, age, salary)
        self.level = level  # extends

    def debug(self):
        print(f"{self.name} is debugging...")

    def work(self):
        print(f"{self.name} is coding...")


class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} is designing...")


se = SoftwareEngineer("max", 20, 8000, "junior")
print(se.name, se.age)
se.work()
se.debug()

# similarly creating a designer instance
de = Designer("phil", 25, 7000)
print(de.name, de.age)
de.work()
de.draw()
