# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# Solution 1
# YOUR CODE GOES HERE:

# for number in range (11,20,2):
#     x = number + x
#     print (x)


# Solution 2

for number in  range (10,20):
    if (number%2) != 0:
        x = x + number
        print("number is even: %s "%number)
        print ("The value of sum is: %s "%x)
    else:
        print ("number is not odd: %s"%number)
