# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

# Run the tests to make sure you've done this correctly!
instructors = ["ColtA","BlueA","LisaA"]

# Append to the list
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
print(instructors)

# Extend the list
instructors.extend(["A","B",12,True])
print(instructors)

# Insert into the list
instructors.insert(3,"ANCD")
print(instructors)

# Clearing a list (removing all the values from the list)
instructors.clear()
print(instructors)

# Creating the list again
instructors = ["ColtA","BlueA","LisaA"]

# find the index in the list where we have mentioned only the value
output = instructors.index("BlueA")
print(output)

# adding more data to the list using extend
instructors.extend([1,12,11,2,4,2,31,12,"ColtA","LisaA","BlueA"])
print(instructors)

# find the index in the list (find the complete list where ever if finds 12)
output = instructors.index(12)
print(output)

# find the index in the list (find the complete list where ever if finds 12 starting from index 6)
output=instructors.index(12,6)
print(output)

# find the index in the list where we have mentioned start and end index
output = instructors.index(12,2,6)
print(output)

# find the count of the number x appears in the list
output = instructors.count(1)
print(output)

# find the count of x in the list 
output = instructors.count("ColtA")
print(output)

# sort the list
# Only the list which has numbers can be sorted not list with strings and numbers
numbers = [1,2,5,3,4,0,12]
numbers.sort()
print(numbers)

# revere the list which are numbers
numbers.reverse()
print(numbers)

# reverse the list which has numbers and strings
instructors.reverse()
print(instructors)

# join method 
# Instructor name
instructors1 = ["ColtA","BlueA","LisaA"]
compsent ='My Name is '.join(instructors1)
print(compsent)
