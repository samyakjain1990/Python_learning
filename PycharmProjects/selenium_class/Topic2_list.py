# Datatype in python 
# https://www.journaldev.com/14036/python-data-types

# List Example 1
ab = ["abc",1,2,2.22]
print (ab)

print(ab[0])
print(ab[1])
print(ab[-1])

# getting data from the list
print(ab[1:3]) # 1,2

print(ab[:2]) # "abc",1

print(ab[1:]) # 1,2,2.2

# appending to the list
ab.append("kind")
print(ab)

ab[1]= 99
print(ab)

# inserting into the list
ab.insert(3,"kinda")
print(ab)

# deleting from the list
del ab[0]
print(ab)

print("############################################")

# List Example 2
test = ["count",112121,22222,34344,3453242342,"you are very kind"]

# This prints the complete list
print(test)

# print 1st element
print(test[0])

# print 2nd element
print(test[1])

# print last element
print(test[-1])

# print 2nd last element
print(test[-2])

# print values from 1 to 4 
print(test[1:4])

# appending to the list
test.append(12)
test.append("NAMAMA")
print(test)

# inserting to the list
test.insert(-1,"Table")
test.insert(1,"First letter")
print(test)

# Deleting from the list
# Trying to delete which does not exist

# just testing try catch to understand :) 
try:
    test.remove("NAMAHA")
except:
    print("I think word does not exist :D ")
    
test.remove("NAMAMA")
print(test)


