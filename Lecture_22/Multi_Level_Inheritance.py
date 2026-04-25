# multi level inheritance

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

class senior_sde(sde): #sde already has class employee 
    def __init__(self,name,age,Id,role,level):
        super().__init__(name,age,Id,role)
        self.level=level

    def __str__(self):
        return super().__str__() + f"\nlevel: {self.level}"

senior_developer= senior_sde("abc",123,25,"sde","2")
print(senior_developer)