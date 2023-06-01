types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_eval = "Isn't that joke so funny?! {}"

print(joke_eval.format(hilarious))

test_variables = "I'm trying to print two variables for format. One is {} and another is {}"

print(test_variables.format(binary, do_not))

print(f"it prints in which order we give it: {test_variables.format(do_not, binary)}")


w = "Part one of the text...."
e = "Now comes part 2 of the text"

print(w+e)