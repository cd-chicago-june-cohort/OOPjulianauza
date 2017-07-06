
class product(object):
    def __init__(self, price, name, weight, brand,cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For sale"
    def sell(self):
        self.status ="Sold"
    def xreturn(self,reason):
        if reason == "like new":
            self.status = "Used"
            self.price -= (self.price*.20)
        else:
            self.status="Defective"
            self.price = 0
    def addTax(self,tax):
        self.price+=(self.price * tax)
    def showInfo(self):
        print "Price:"+str(self.price)
        print "Name:"+str(self.name)
        print "Weight:"+str(self.weight)
        print "Brand:"+str(self.brand)
        print "Cost:"+str(self.cost) 
        print "Status:"+str(self.status)
        return self
    
product1=product(4,"Sponge",".4oz","Sephora",.80)
product1.showInfo()
product1.xreturn("like new")
product1.showInfo()
product1.addTax(.50)
print product1.price
        




        