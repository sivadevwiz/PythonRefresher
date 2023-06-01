print("we are seeing more printing in this exercise")
print("We are going to use the format command {} without a variable but a string.".format("test"))


print("Now we will multiply the text")
print("*" * 10)

end1 = "N"
end2 = "E"
end3 = "W"
end4 = "H"
end5 = "O"
end6 = "P"
end7 = "E"

# Below will not work
#print(end1 + end2 + end3, end=" ", end4 + end5 + end6 + end7 + end8 )

#NEW
#HOPE
print(end1 + end2 + end3)
print(end4 + end5 + end6 + end7)

#NEWHOPE
print(end1 + end2 + end3, end="")
print(end4 + end5 + end6 + end7)

# NEW HOPE
print(end1 + end2 + end3, end=" ")
print(end4 + end5 + end6 + end7)

# ERROR: TypeError: 'test' is an invalid keyword argument for print()
# print(end1 + end2 + end3, test=" ")
# print(end4 + end5 + end6 + end7)

#Because end is a parameter of the print

print("this is a new line", end="End parameter content")