#revision
class complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #self.count=0 ->not working , problem for later

    def details(self):
        #self.count+=1
        return f"{self.x} + {self.y}i"

    def __add__(self,other):
        other.x=self.x+ other.x
        other.y=self.y+ other.y
        return other


c1=complex(2,4)
print(c1.details())
c2=complex(3,5)
print(c2.details())
c2=c1+c2
print(c2.details())
#print(c2.count()) #as the count is not a method we dont have to put () after c2.count