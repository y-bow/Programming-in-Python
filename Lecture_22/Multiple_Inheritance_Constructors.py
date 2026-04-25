class A:
    def __init__(self, name):
        self.name = name
        print("Constructor A has been created")
        
class B:
    def __init__(self, age):
        self.age = age
        print("Constructor A has been created")

class C(A,B):
    def __init__(self, name, age):
        A.__init__(self, name)
        B.__init__(self, age)
        print("Constructor C has been created")
    def __str__(self):
        return f"Name : {self.name} \n Age : {self.age}"
    
c = C("abc", 20)
print(c)