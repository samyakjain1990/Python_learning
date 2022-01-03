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

# Extend to the list
instructors.extend(["A","B",12,True])
print(instructors)


# Insert to the list
instructors.insert(3,"ANCD")

print(instructors)

# Clearing a list

instructors.clear()
print(instructors)