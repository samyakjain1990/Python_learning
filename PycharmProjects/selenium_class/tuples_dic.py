ab = ("abc",1,2,2.22)
print (ab)

print(ab[0])
print(ab[1])
print(ab[-1])

# getting data from the tuple
print(ab[1:3]) # 1,2

# appending to the tuple
#ab.append("kind")
#print(ab)

# inserting into the list
#ab.insert(3,"kinda")
#print(ab)

# deleting from the list
#del ab[0]
#print(ab)

# Dict

abc ={1:"abc",2:"new",3:"key"}

print(abc[1])

# playing with dict

key = input("Enter the value of key:")
value = input("Enter the value for the key:")

dict= {}

dict[key]= value

print(dict)