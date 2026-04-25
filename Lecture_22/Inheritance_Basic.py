class employee:
    def __init__(self,name,Id,age):
        self.name=name
        self.Id=Id
        self.age=age
        
    def get_details(self):
        print(f"Nme: {self.name} \nId: {self.Id}  \nage: {self.age}")

class sde(employee):#inherit class employee (all its attribute and method)
    def  __init__(self,name,Id,age,role):#we dont have to define it 
        super().__init__(name,Id,age)#we are calling init from employee
        self.role=role
        
    def get_details(self): #repeated
        print(f"Nme: {self.name} \nId: {self.Id}  \nage: {self.age} \nrole: {self.role}")

se1=sde("abc",123,23,"sde")
se1.get_details()