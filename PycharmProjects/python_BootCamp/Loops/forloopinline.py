# Example: Print the even numbers by adding 1 to the odd numbers in the list

# odd = [1, 5, 7, 9]

# for num in odd:
# 	if (num%2 !=0):
# 		new_num = num +1
# 		print(new_num)


# even = [num + 1 for num in odd if num%2!=0]
# print(even)


#Example 1: Access all characters of a string
#=============================================

# text = "samyak"

# for cha in text:
# 	print(cha,end=' ')

# Example 2: Iterate string in reverse order

# print(' ')

# for cha in reversed(text):
# 	print(cha,end=' ')


# Example 3: Iterate over a particular set of characters in string
#==================================================================


# sent= "my name is samyak Jain"
# for cha in sent[2:10:1]:
# 	print (cha,end=' ')


#Example 5: Iterate over words in a sentence using the split() function
#=======================================================================

# for cha in sent.split():
# 	print(cha)


# numbers = [1,2,4,6,7]
# players = ["Messi", "Ronaldo", "Neymar"]


# for num in numbers:
# 	print(num)

# for num in players:
# 	print (num)


# dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
# for key in dict1:
#     print(key,"-->",dict1[key])

#Example 5: Iterate only the values the dictionary
#=================================================
dict1 = {"Brand": "BMW", "Color": "Black", "Date": 1964}

for value in dict1.values():
	print(value)
