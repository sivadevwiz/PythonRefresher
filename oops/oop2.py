"""
Functions in classes
"""


# consider the below example

# se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
# se2 = ["Software Engineer", "Lisa", 25, "Junior", 7000]
#
# d1 = ["designer", "Phil", 30]
#
#
# def code(se):
#     print(f"{se[1]} is writing code")
#
#
# code(se1)
# code(se2)
# code(d1)  # here designer is also making use of this method


# in this example
# instance method
# arguments and return values
# dunder methods - double underscore methods
# @staticmethod

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

    # instance method
    # self parameter refers to the instance
    def code(self):
        print(f"{self.name} is writing code")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # the below method can be replaced by the __str__ method which is a special or dunder method
    #     def information(self):
    #         information = (f"""********************
    # Information:
    # Name: {self.name}
    # Age: {self.age}
    # Level: {self.level}
    # Pay: {self.pay}
    # ********************""")
    #         return information

    # Dunder method - which has a leading and trailing underscores
    # they have a default implementation along with the class
    # if we explicitly mention them the default implementation will be overriden
    def __str__(self):
        information = (f"""********************
Information:
Name: {self.name}
Age: {self.age}
Level: {self.level}
Pay: {self.pay}
********************""")
        return information

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True

    @staticmethod
    def entry_salary(age): # here self is not required
        match age:
            case 26:
                return 7000
            case 27:
                return 8000
            case 28:
                return 9000
            case _:
                return 0


# instance
se1 = SoftwareEngineer("Siva", 34, "TL", 40)
se2 = SoftwareEngineer("MAx", 34, "TL", 40)
se3 = SoftwareEngineer("MAx", 34, "TL", 40)

se1.code()
se2.code()

se1.code_in_language("python")
# print(se1.information())
print(se1)
print(se2)

print(se2 == se3)

print(se1.entry_salary(26))
print(SoftwareEngineer.entry_salary(28))
