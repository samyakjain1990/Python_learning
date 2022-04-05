'''
Topic to understand from here:
a) how to create a class
b) creating object for a class
c) calling method using object
d) what is default contructor
e) printing from a method 
'''

class Calculator:
    num = 1                          # Class variables

    def getdata(self):
        print("Just learning the classes")

obj = Calculator()                  # create obj in python

obj.getdata()
print(obj.num)


print("Learning default contructor****************")


class Calce:
    # default constructor

    def __init__(self):
        print("Called automaticallly")

    def textprint():
        print("Seomthing to be printed")


newobj = Calce()

Calce.textprint()