# Printing the format string variables

# String with variables embedded in them

# We must start the string with the letter f for "format"
# Example: f"Hello {name}"


name = 'Sivasankaran'
age = 34 #just turned
height = 174 #cm
weight = 93 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

cm_to_inches = 2.54
kg_to_pounds = 2.20462

some_number = 34.5

print(f"Some number........ {round(some_number)}")

print(f"My name is {name}")
print("My name is {name}") # Without adding f we cannot embed a variable inside another variable

print(f"My age is {34} and I'm {height}cm tall")
print(f"My height will be {round(height / cm_to_inches, 2)} inches")

print(f"I'm {weight}kg heavy")
#Study drill
print(f"It will be {round(weight * kg_to_pounds, 2)} lbs in pounds")
print("Yes need to reduce it")
print(f"My eyes are {eyes} and my hair color is also {hair}")
print(f"My teeth are {teeth} and depends on the coffee")

weird_total = age + height + weight

print(f"If I add {age}, {height}, {weight}, I will get {weird_total}")
