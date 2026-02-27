class complex:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, others_object):
        c1 = complex()
        c1.x = self.x + others_object.x
        c1.y = self.y + others_object.y
        return c1
    
    def __mul__(self, others_object):
        c1 = complex()
        c1.x = (self.x * others_object.x) - (self.y * others_object.y)
        c1.y = (self.x * others_object.y) + (self.y * others_object.x)
        return complex(c1.x,c1.y)

    def details(self):
        print(f"{self.x} + {self.y}i")

c1 = complex(1,2)
c1.details()
c2 = complex(3,2)
c2.details()
c3 = c1 + c2
c3.details()
c3 = c1 * c2
c3.details()
