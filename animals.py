class animals(object):
    def __init__(self,name):
        self.name = name
class dog(animals):
    health = 150
    def walk(self):
        self.health-=1
    def run(self):
        self.health-=5
    def pet(self):
        self.health+=5
    def showHealth(self):
        "Health is:",self.health,"I'm a Dog!"
class dragon(animals):
    health = 170
    def fly(self):
        self.health-=10
    def showHealth(self):
        print "Health is:",self.health,"I'm a Dragon!"

animal=dog("doggy")
animal.walk()
animal.walk()
animal.walk()
animal.run()
animal.run()
animal.pet()
#animal.fly() returns error
animal.showHealth()


animal1=dragon("draggy")
animal1.fly()
animal1.fly()
#animal1.pet() returns error
animal1.showHealth()


        
        




        