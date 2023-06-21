def outer_function():
    numbers = []

    def inner_function(x):
        numbers.append(x)
        print(numbers)

    return inner_function


num = outer_function()
num(3)


#  The above function can be rewritten into class as follows

class outer:
    numbers = []

    def inner_function(self, x):
        self.numbers.append(x)
        print(self.numbers)


# creating object of class
num2 = outer()
num2.inner_function(5)


# another way of calling
outer().inner_function(10)


""""
Example 2
"""

# def outer_function(x):
#     def inner_function1(y):
#         def inner_function2(z):
#             return x + y + z
#         return inner_function2
#     return inner_function1
#
#
# closure = outer_function(1)
# result = closure(2)(3)
# print(result)

""""
Example 3
"""


# def outer_function(x):
#     def inner_function():
#         print("Enclosed variable x:", x)
#
#     def inner_method():
#         print("Enclosed method")
#
#     return inner_function, inner_method
#
#
# closure = outer_function(10)
# closure_variables, closure_method = outer_function(10)
# closure_variables()  # Output: Enclosed variable x: 10
# closure_method()  # Output: Enclosed method


""""Example 4"""

g_count = 3
list = []
def count():
    count = 10
    global g_count
    g_count += 1
    print("g_count....", g_count)

    def increment():
        # global list
        # list.append(12)
        global g_count
        nonlocal count
        g_count = g_count + 1 # TypeError: unsupported operand type(s) for +: 'function' and 'int' when global is not mentioned within count
        # g_count = 24 # 24
        count += 1
        print(list)
        print("g_count....", g_count)
        print(count)

    increment()

count()
