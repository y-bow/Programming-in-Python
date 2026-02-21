#Magnitude
class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        print(f"{(self.x**2 + self.y**2)**0.5}")

c1 = complex(1,2)

c1.mag()