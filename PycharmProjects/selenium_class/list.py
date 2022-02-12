ab = ["abc",1,2,2.22]
print (ab)

print(ab[0])
print(ab[1])
print(ab[-1])

# getting data from the list
print(ab[1:3]) # 1,2

# appending to the list
ab.append("kind")
print(ab)

# inserting into the list
ab.insert(3,"kinda")
print(ab)

# deleting from the list
del ab[0]
print(ab)
