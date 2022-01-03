
# list is the similar to array but in list you can store than 1 variable with different datatype.We cannot add mrore data in the list.

list = [12,'my name',2.23,70.1]
minilist = [22.0,'david','milk']

print(list)
print(list[1:3])
print(list[3])
print(list[1:])
print(minilist * 3)
print(list + minilist)


# Tuples are similar to list but in this we can add more data even after it is created.they can be called as read-only list

tuple = ('lion',12,'12-D','Dust')
tinytuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple + tinytuple)


# Dictionary are a kind of hash-table.they consist of key-pair value.they are ususally inordered

dict = {}
dict['one']='the value of this one'
dict[2] = "The valus is 2"
dicttiny ={'name':'samyak','BU':'CCBU','EmpID':347467}

print(dict['one'])
print(dict[2])
print(dicttiny)
print(dicttiny.keys())
print(dicttiny.values())

