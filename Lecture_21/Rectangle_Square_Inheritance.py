class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class square(rectangle):
    def __init__(self,side):
        self.side=side
    def area_1(self):
        return self.side**2

s1=square(5)
print(s1.area_1())