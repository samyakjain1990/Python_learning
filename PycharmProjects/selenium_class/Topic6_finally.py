
from logging import exception


items = input("Enter the value of items:")


# Failed Block
try:
    if items !=2 :
        raise Exception("The numbers are not matching")
    else:
        print("The numbers are fine")

except:
    print("Look like it failed in number matching")

finally:
    print("text printing")

# one more example

try:
    with open('txt.abc','r') as reader:
        reader.readline()

except Exception as e :
    print (e)

finally:
    print("finally is printed")