"""
OOP Exercise 4: Class Inheritance

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
"""


class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# inherting the Vehicle class in bus
class bus(Vehicle):
    # here we are going to overriding the seating_capacity method 
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

if __name__ == "__main__" :
    obj = bus("Volvo",80,50)
    print(obj.seating_capacity())