"""
Polymorphism -

types:
Compile-time polymorphism (static polymorphism), occurs when a function or method can be called with different arguments
of different types, but the compiler can determine the correct implementation at compile time.
 For example, the print() function in Python can be used to print objects of different types, such as strings, integers,
and lists.

Run-time polymorphism (dynamic polymorphism), occurs when a function or method can be called with different arguments
of different types, and the correct implementation is determined at run time.
 For example, the draw() method in a graphics library can be used to draw different shapes, such as circles, squares,
 and triangles.

"""


# parent or base class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working....")


class SoftwareEngineer(Employee):
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


# polymorphism

employees = [
    SoftwareEngineer("max", 20, 8000, "junior"),
    SoftwareEngineer("Lisa", 30, 8000, "Senior"),
    Designer("phil", 25, 7000)
]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employees)
