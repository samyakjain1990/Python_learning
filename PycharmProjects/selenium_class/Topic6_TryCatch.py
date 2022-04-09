

items = input("Enter the value of items:")


# Failed Block
try:
    if items !=2 :
        raise Exception("The numbers are not matching")
    else:
        print("The numbers are fine")

except:
    print("Look like it failed in number matching")

# testing working block

try:
    if items ==23 :
        raise Exception("The numbers are not matching")
    else:
        print("The numbers are fine")

except:
    print("Look like it failed in number matching")


try:
    if items !=3 :
        raise Exception("The numbers are not matching")
    else:
        print("The numbers are fine")

except Exception as e :
    # here e will print the exception from the above if block
    print (e)
    print("Look like it failed in number matching")
