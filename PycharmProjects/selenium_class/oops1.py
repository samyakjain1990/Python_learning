# self keyword is imp for calling variable names in method
# instance variable cannot be chnaged in the class whereas the instance variable can be chnaged at runtime
# contructor name is always __init__

print("Learning Parameterized contructor****************")

class newCalulator:
    x = 102

    def __init__(self,a,b):
        self.aa = a
        self.bb = b
    
    def sumcal(self):
        #cc = self.aa + self.bb + self.x  #1st way of calling "x" variable 
        cc = self.aa + self.bb + newCalulator.x # second way of calling class varible
        return cc



if __name__ == "__main__":

    objnum = newCalulator(1,2)

    print(objnum.sumcal())

    objnum2 = newCalulator(2,5)
    print(objnum2.sumcal())