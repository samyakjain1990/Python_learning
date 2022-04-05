'''
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''

class Vehicle:

    def __init__(self,max_speed,milage):
        self.max_speed = max_speed
        self.milage = milage

if __name__ == "__main__" :
    obj_class = Vehicle(23,121)
    print(obj_class.max_speed,obj_class.milage)


'''
OOP Exercise 2: Create a Vehicle class without any variables and methods
'''

class Vehicle1:
#   Pass is used when a statement is required syntactically but you do not want any command or code to execute
    pass
