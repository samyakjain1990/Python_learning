
# Printing a basic hello text
print("Hello")

# Playing with numbers
a = 10
b = 20
print(a)
print(b)

c = a +b
print(c)

d , e , f ,g= 1,10,"abc","Kind"

# Here we are printing letter but not numbers so print is diff
print("The value of f :"+f)
print("The Value of g :"+g)

# This is the incorrect way of printing number when you are concatinating to one sentence
# number cannot be added to an string 
# print("The value of a:"+a)

# This is the correct way of printing number when you are prining numbers 
# print the value of a which is int and concatinating is giving an error
print("{} {}".format("The value of d :",d))
print("{}{}".format("The value of e :",e))

print("{}{}".format("The value of c:",c))

print(type(a))

