filename = "sample.txt"
#
# try:
#     file = open(filename, "r")
#     content = file.read()
#     print(file.closed)  # to check if file is closed
#     print(content)
# finally:
#     file.close()
#     print("end of code")
#     print(file.closed) # to check if file is closed

# alternate way with "with"

with open(filename, "r") as file:
    content = file.read()
    print(file.closed)  # to check if file is closed
    print(content)

print(file.closed)
