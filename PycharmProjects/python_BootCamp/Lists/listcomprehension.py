
numbers = [1,2,3,4,5,6,7]

# Example - 1
#==============
double_numbers = []

for num in numbers:
    double_number = num *2
    double_numbers.append(double_number)

print(double_numbers)

# another way of doing it using comprehension
double_numbers1 = [num * 2 for num in numbers]

print(double_numbers1)

# Example - 2
#=============
name = ["colt"]

for char1 in name:
    uppername = char1.upper()
    print(uppername)

uppername1 = [char2.upper() for char2 in name]
print(uppername1)

group = ["john","test","maximum"]
group1 = [group2[0].upper() for group2 in group]

print(group1)

# Example - 3
#==============
# we can use comprenhention with list also
rangeex = [numb * 2 for numb in range(1,10)]
print(rangeex)

# example - 4
#===============
# converting to bool val
boolex = [bool(val) for val in [False,True,[],0]]
print(boolex)

# example - 5
#================
# convert number to strings
convertnum = [str(num) for num in numbers]
print(convertnum)

# example - 6
#=============
# we can even add text to strings

convertnum = [str(num)+ "Hey" for num in numbers]
print(convertnum)


# example - 7
#==============
#  adding conditional logic in the lists
checknumifeven = [num for num in numbers if num%2 == 0]
checkforodd = [num for num in numbers if num%2 != 0]
print(checknumifeven)
print(checkforodd)




