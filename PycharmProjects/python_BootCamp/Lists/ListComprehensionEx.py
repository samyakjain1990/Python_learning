# Example : 1
#==============

namelist = ["Elie","Tim","Matt"]
answer = [char[:1] for char in namelist]
print(answer)

numlist = [1,2,3,4,5,6]
answer2 = [numb for numb in numlist if numb%2 ==0 ]
print(answer2)

# Another way of doing this 

namelist = ["Elie","Tim","Matt"]
answer = [char[0] for char in namelist]
print(answer)

numlist = [1,2,3,4,5,6]
answer2 = [numb for numb in numlist if numb%2 ==0 ]
print(answer2)


# Example : 2
#==============
list1 = [1,2,3,4]
list2 = [3,4,5,6]
answer = [num for num in list1 if num in list2]
print(answer)

listname = ["Elie","Tim","Matt"]
listlower = [listnam.lower() for listnam in listname]
answer2 = [listre[::-1] for listre in listlower]
print(answer2)

# Another way of dong this 
answer2 = [listre[::-1].lower() for listre in listname]