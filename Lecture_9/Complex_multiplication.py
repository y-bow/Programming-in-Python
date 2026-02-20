#Multiplication
class complex:
    def __init__(self, x, y): #Constructor ( Special Method )
        self.x = x
        self.y = y
    def details(self): #Method
        print(f"{self.x} + {self.y}i")
    def mult(self, others):
        real = (self.x * others.x) - (self.y * others.y)
        imag = (self.x * others.y) + (self.y * others.x)
        return complex(real,imag)

c1 = complex(1,2)
c1.details()
c2 = complex(3,2)
c2.details()
c1 = c1.mult(c2)
c1.details()