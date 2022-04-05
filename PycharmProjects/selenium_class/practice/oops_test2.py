'''
OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Output format : Vehicle Name: School Volvo Speed: 180 Mileage: 12

'''

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Bus is a child  class of vehicle
class bus(Vehicle):
    pass
    
if __name__ == "__main__" :
    obj_class = bus("School Volvo",121,12)
    print("Vehicle Name:",obj_class.name,"Speed:",obj_class.max_speed,"Mileage:",obj_class.mileage)