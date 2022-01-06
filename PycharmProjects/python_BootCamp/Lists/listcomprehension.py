
numbers = [1,2,3,4,5,6,7]

# Example - 1
#==============
double_numbers = []

for num in numbers:
    double_number = num *2
    double_numbers.append(double_number)

print(double_numbers)

# another way of doing it
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