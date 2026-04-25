class employee:
    def __init__(self,name,age,Id):
        self.name=name
        self.Id=Id
        self.age=age
        
    def get_details_1(self):
        print(f"Nme: {self.name} \nId: {self.Id}  \nage: {self.age}")

class sde(employee):
    def __init__(self,name,age,Id,role):
        super().__init__(name,Id,age)
        self.role=role
        
    def get_details_2(self):
        super().get_details_1() #Same thing
        print(f"role: {self.role}")

se1=sde("xyz",234,14,"sde_1")
# se1.get_details_1()
se1.get_details_2()