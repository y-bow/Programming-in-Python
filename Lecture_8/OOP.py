#Syntax of class
class cylinder:
    def __init__(self,h,r): #constructor (it is a special type of function)
        self.h = h #attribute or data member
        self.r = r #attribute or data member
    def volume(self): #member function or method
        return 3.14*self.h*(self.r**2)
    def surface_area(self): #member function or method
        return 2*3.14*self.h*self.r

c1 = cylinder(1,1)
c2 = cylinder(2,2)

#How to call a method on c1

print(c1.volume())
print(c1.surface_area())