""""
# ================
# slicing in Python
# ================= 

# Slicing can be applied to the below :
# 1) List DataStructure
# 2) String

# syntax for slicing is [start:end:step]
# Note : value of starting index will always be taken in consideration for 
# the output but not the value present in the ending index 
"""
#=======
# lists
#=======

number = [1,2,5,3,4,0,12]
number1 = number[:3]   #:3 means in the given list all the values towards to the left from 3 will be selected
print(number1) 

number2 = number[2:]   #2: means in the given list all the values towards to the right from 2 will be selected
print(number2)

number3 = number[2:5:] #2:5: means in the given list all the values b/w index 2 and 5 will be selected
print(number3)

number4 = number[1:6:2] #1:6:2 means in the given list all the values b/w index 1 and 6 will be selected  with a step of 2
print(number4)

# The same can be done with String stored in the List

text1 = ["My","name","is","samyak","jain"]

text2 = text1[:3]
print(text2)

text3 = text1[3:]
print(text3)

text4 = text1[1:3:2]
print(text4)

#==========
# Strings
#==========
text = ("My name is samyak jain")

slicetext = slice(3)    # Stop at one index "slice(stop)"
print(text[slicetext])

slicetext1 = slice(1,8,2)   # Start stop and step "slice(start, stop, step)"
print(text[slicetext1])

"""
OUTPUT
samyjain@SAMYJAIN-M-K1YX Python_learning % /usr/local/bin/python3 /Users/samyjain/Python_learning/PycharmProjects/slicing.py
[1, 2, 5]
[5, 3, 4, 0, 12]
[5, 3, 4]
[2, 3, 0]
['My', 'name', 'is']
['samyak', 'jain']
['name']
My 
ynm
"""