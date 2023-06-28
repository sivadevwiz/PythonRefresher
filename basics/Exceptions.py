""""
we put the code within the try block and check for error with except block
else and finally are other blocks
else will run as else case
finally will run either ways
"""

try:
    a = 5 / 0
except Exception as e:
    print(e)

try:
    result = 2 / 0
    print(result)
except ZeroDivisionError as e:
    # print("ZeroDivisionError found")
    print(e)
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


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = f"{message} = {value}"
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)


try:
    test_value(4)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    if hasattr(e, 'message'):
        print(True)
    else:
        print(False)
    print(e)
    # print(e.message, e.value)
