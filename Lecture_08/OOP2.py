#Syntax of class
class human:
    def __init__(self,n,a,s): #constructor (it is a special type of function)
        self.n = n
        self.a = a
        self.s = s
    def name(self): #member function or method
        return self.n
    def age(self): #member function or method
        return self.a
    def school(self):
        return self.s

h1 = human("Person1", 18 , "SCDS")

print(h1.name())