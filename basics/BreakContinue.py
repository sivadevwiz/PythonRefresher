items = [1, 2, 3, 4, 5]

# Continue skips the code after it but continues the loop
for item in items:
    if item == 2:
        continue
    print(item)

# Break skips the code after it and also breaks the loop
for item in items:
    if item == 3:
        break
    print(item)
