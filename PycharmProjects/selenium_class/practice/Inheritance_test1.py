from oops_test2 import Vehicle

class Truck(Vehicle):

    def __init__(self):
        Vehicle.__init__(self,"Test", 80, 23)

    def test():
        a = 676
        return a


if __name__ == "__main__":

    obj = Truck()
    print(obj.test())
