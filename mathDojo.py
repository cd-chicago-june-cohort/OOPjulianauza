
class Mathdojo(object):
    def __init__(self):
        self.total=0
    def add(self, *num):
        for x in num:
            self.total+= x
        return self
    def subtract(self, *num):
        for x in num:
            self.total-= x
        return self
    def result(self):
        print self.total
        return self

md = Mathdojo().add(2).add(2, 5).subtract(3, 2).result()







        
        




        