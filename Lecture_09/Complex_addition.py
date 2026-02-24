#Addition
class complex:
    def __init__(self, x, y): #Constructor ( Special Method )
        self.x = x
        self.y = y
    def details(self): #Method
        print(f"{self.x} + {self.y}i")
    def add(self, others):
        others.x = self.x + others.x
        #  c2.x  =  c1.x  +  c2.x
        others.y = self.y + others.y
        #  c2.y  =  c1.y  +  c2.y
        return others

c1 = complex(1,2)
c1.details()
c2 = complex(3,2)
c2.details()
c1 = c1.add(c2)
c1.details()