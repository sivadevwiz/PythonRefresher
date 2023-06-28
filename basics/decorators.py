# def fact_text(func):
#     def wrapper(*args, **kwargs):
#         print("before")
#         val = func(*args, **kwargs)
#         print("after")
#         return val
#
#     return wrapper
#
#
# @fact_text
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Do something before the function is called
#         print("Before the function is called")
#
#         # Call the function
#         result = func(*args, **kwargs)
#
#         # Do something after the function is called
#         print("After the function is called")
#
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))

# def log_time(func):
#     """"method to logtime"""
#     def wrapper():
#         print("before")
#         val = func()
#         print("after")
#         return val
#     return wrapper()
#
#
# @log_time
# def test_func():
#     print("Test func")

# Example from another tutorial
# Decorator with arguments

import functools
#
# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper
#
# @start_end_decorator
# def print_name():
#     print("Name")
#
#
# @start_end_decorator
# def add5(x):
#     return x + 5
#
#
# # print_name = start_end_decorator(print_name) #equaivalent of adding the decorator
#
# # print_name()
#
# # print(add5(10))
# print(help(add5))
# print(add5.__name__)

"""
Decorator with parameter and nested
"""
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = ""
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
#
#
# @repeat(num_times=3)
# def greet(name):
#     print(f"Hi {name}")
#
#
# greet("Bond")


"""
Stacking decorators
"""

# def start_end_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("end")
#         return result
#     return wrapper
#
#
# def start_text(func):
#     def wrapper(*args, **kwargs):
#         print("Start text start")
#         result = func(*args, **kwargs)
#         # result = "The name is going to be displayed"
#         print("Start text end")
#         return result
#     return wrapper
#
#
# @start_text
# @start_end_decorator
# def say_hello(name):
#     greeting = f"Hello {name}"
#     print(greeting)
#     return greeting
#
#
# say_hello("Bond")


"""
Class decorator
"""

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} time{'s' if self.num_calls > 1 else ''}")
        return self.func(*args, **kwargs)


# cc = CountCalls(None)
# cc()


@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()



