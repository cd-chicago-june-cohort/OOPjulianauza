

class car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def displayinfo(self):
        print "Price is: " + str(self.price)
        print "Speed is: ",self.speed
        print "Fuel: "+str(self.fuel)
        print "Mileage: "+str(self.mileage)  
        if self.price > 10000:
            print "Tax: 15%"
        else:
            print "Tax: 12%"


# create instances and run methods
car1 = car(5000,30,"full",12)
car1.displayinfo()




        