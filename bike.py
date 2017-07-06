

class Bike(object):
    def __init__(self,price,maxspeed):
        self.maxspeed = maxspeed
        self.price = price
        self.totalmiles = 0
    def displayinfo(self):
        print "Price is: " + str(self.price)
        print "Max Speed is: "+ str(self.maxspeed)
        print "Total miles: "+str(self.totalmiles) 
    def drive(self):
        print "Driving" 
        self.totalmiles+=10
    def reverse (self):
        print "reverse"
        if self.totalmiles >= 5:
            self.totalmiles-= 5

# create instances and run methods
bike1 = Bike(100.00, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(200.00, 20)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

        