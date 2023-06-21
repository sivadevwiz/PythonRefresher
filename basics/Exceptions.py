""""
we put the code within the try block and check for error with except block
else and finally are other blocks
else will run as else case
finally will run either ways
"""


try:
    result = 2 / 0
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError found")
except:
    print("Default error found")
else:
    print("else block")
finally:
    result = 1
    print("end of code")

print(result)

class CustomException(Exception):
    print("inside")
    pass

try:
    raise CustomException()
except CustomException:
    print('CustomException')





