from re import X
from Topic4_oops1 import newCalulator

class newwcalculator(newCalulator):
    dummy = 100

    def __init__(self):
        newCalulator.__init__(self,222, 1)

    def getdatafromclass(self):
        c = self.dummy +self.sumcal()
        print (c)


if __name__  == "__main__":

    objdummy = newwcalculator()

    objdummy.getdatafromclass()
