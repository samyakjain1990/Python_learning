# Tuples

ab = ("abc",1,2,2.22)
print (ab)

print(ab[0])
print(ab[1])
print(ab[-1])

# getting data from the tuple
print(ab[1:3]) # 1,2

# appending to the tuple
# Tupple does not support append
#ab.append("kind")
#print(ab)

# inserting into the list
#ab.insert(3,"kinda")
#print(ab)

# deleting from the list
#del ab[0]
#print(ab)

# Dict

print("#################DICT#####################")

abcd ={1:"abc",2:"new",3:"key"}

print(abcd[1])

# playing with dict

dictb= {}

dictb["name"] = "samyak"
dictb["age"] = 31
dictb["location"] = "delhi"

print(dictb)

key = input("Enter the data for key:")
value = input("Enter the data for value:")

dicta= {}

dicta[key]= value

print(dicta)