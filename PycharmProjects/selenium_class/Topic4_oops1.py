'''
Topic to understand from here:
a) creating parameterized constuctor
b) about intance variables
c) how to use class variables & instance variables
'''


# self keyword is imp for calling variable names in method
# instance variable cannot be chnaged in the class whereas the instance variable can be chnaged at runtime
# contructor name is always __init__

print("Learning Parameterized contructor****************")

class newCalulator:
    x = 102

    # here a and b are instance variables 
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def sumcal(self):
        #cc = self.aa + self.bb + self.x  #1st way of calling "x" variable 
        cc = self.a + self.b + newCalulator.x # second way of calling class varible
        return cc



if __name__ == "__main__":

    objnum = newCalulator(1,2)

    print(objnum.sumcal())

    objnum2 = newCalulator(2,5)
    print(objnum2.sumcal())