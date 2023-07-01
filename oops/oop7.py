"""
Properties

Pythonic way of adding getter and setter
"""


class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    # Getter - will have a complete name and property decorator will be added
    @property
    def salary(self):
        return self._salary

    # Setter - will also have a complete name and same as the getter; decorator of the name and setter will be added
    @salary.setter
    def salary(self, value):
        self._salary = value

    # Deleter
    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer()

# with getter and setter
# se.set_salary(5000)
# print(se.get_salary())

# with the pythonic implementation

se.salary = 5000
print(se.salary)

# to check deleter
# del se.salary
# print(se.salary) #AttributeError: 'SoftwareEngineer' object has no attribute '_salary'

