"""
Encapsulation - mechanism of hiding the data implementation

instance variables are kept private and only one accessor method from the outside with which we can access or change
instance variables.
we restrict the access to the public methods - getter and setter methods
instance methods are kept private

getters and setters - only way to access the protected attributes from outside the class
Reason - we can add more function to them than just setting or getting the value of it
"""

"""
Abstraction - each object should only expose the  high level mechanism for using it and hide the internal implentation
"""


class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None  # internal (protected) attributes start with _ (underscore)
        # self.__salary = None  # private attributes start with __ (double underscore)
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    # Getter
    def get_salary(self):
        return self._salary

    # Setter
    def set_salary(self, base_value):
        # sample functionality

        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if 10 < self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Max", 20)

print(se.name, se.age)  # Max 20
print(se.name, se.age, se._salary)  # Max 20 None # internal variable can be accessed
# print(se.name, se.age, se.__salary) # AttributeError: 'SoftwareEngineer' object has no attribute '__salary'

for i in range(80):
    se.code()

# print(se._num_bugs_solved)

se.set_salary(5000)

print(se.name, se.age, se.get_salary())  # Max 20 5000




