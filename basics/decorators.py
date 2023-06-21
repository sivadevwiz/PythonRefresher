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

def log_time(func):
    """"method to logtime"""
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper()


@log_time
def test_func():
    print("Test func")



