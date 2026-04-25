#using DUNDER method -> double underscore method

class employee:
    def __init__(self,name,age,Id):
        self.name=name
        self.Id=Id
        self.age=age
        
    def __str__(self):
        return f"Nme: {self.name} \nId: {self.Id}  \nage: {self.age}"

class sde(employee):
    def __init__(self,name,age,Id,role):
        super().__init__(name,Id,age)
        self.role=role
        
    def __str__(self):
        return super().__str__() + f"\nrole: {self.role}"

se1=sde("xyz",234,14,"sde_1")
print(se1)