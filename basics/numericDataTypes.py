# Complex numbers - which has real and imaginary numbers

complex_num = 1 + 3j

complex_num2 = complex(1, 3)

print("complex_num..............", complex_num)
print("complex_num2..............", complex_num2)

print("complex_num.real", complex_num.real)  # 1.0
print("complex_num.imag", complex_num.imag)  # 3.0

print("type(complex_num)................", type(complex_num))

sum = complex_num + complex_num2

print("sum..........", sum)
print("prod..........", complex_num * complex_num2)