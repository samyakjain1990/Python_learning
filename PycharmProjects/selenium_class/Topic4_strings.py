from posixpath import split

str1 = "My name is . Samyak Jain "
str2 = " Ashram"

print(str1[1])

print(str1[0:9])

print(str1[0:16])

values = "Samyak Jain"
plus = str1 + str2

print(values[0:])
print(values[-1:])

print(plus)
print(values in str1)

var = str1.split(".")
print(var)

# printing the first word after .
print(var[0])

# printing the second word after .
print(var[1])

# Stripping the space
print(var[1].strip())

# stripping the left space
print(var[1].lstrip())

# stripping the right space
print(var[1].rstrip())