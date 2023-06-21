# Recursion - Recursive function - Calls the same function again

# Taking the example of calculating factorial
# text = ""
# text_list = []
#
#
#
# def factorial(n):
#     global text
#     global text_list
#     final_list = text_list
#     if n == 1:
#         text += str(n)
#         print("textf.........", text)
#         final_list.append(text)
#         print("end")
#         return 1
#     text += str(n) + " * "
#     print("text.........", text)
#     return final_list, (n * factorial(n - 1))


# fact_text, fact_val = factorial(5)
# print("fact_text", fact_text[0])
# print("{text} = {result}".format(text=text_list[0], result=factorial(5)))
# print("{text} = {result}".format(text=fact_text[0], result=fact_val))

# def get_text_and_number():
#     text = "This is a text."
#     number = 123
#     return text, number
#
#
# par1, par2 = get_text_and_number()
#
# print(par1, par2)


# def factorial(n):
#     if n == 1:
#         return 1
#     return (n * factorial(n - 1))
#
# print(factorial(5))


def factorial(n):
    def fact_val(n):
        if n == 1:
            return 1
        return (n * fact_val(n - 1))

    val = fact_val(n)

    def fact_text(n):
        text = ""

        while n > 0:
            text += str(n) + " * "
            n -= 1

        return text[:-2]

    text = fact_text(n)
    print("text", text)

    return text, val


# factorial(5)

text, val = factorial(5)
print(text)
print(val)
