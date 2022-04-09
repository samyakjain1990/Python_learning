# As a part of this topic we will learning how to read a file
# when you need to read a file either use read() or readline() do not use them together (it makes things complicated)
file = open('ReadText.txt')

# can read the complete file
#print(file.read())

# readline reads line by line
print(file.readline())

print(file.readline())

file.close()