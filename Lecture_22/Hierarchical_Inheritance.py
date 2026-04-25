#multiple inheritance

class member:
    def __init__(self,name,Id,age):
        self.name=name
        self.Id=Id
        self.age=age

    def __str__(self):
        return f"name: {self.name}\nage: {self.age}\nID: {self.Id}"

class student(member):
    def __init__(self,name,Id,age,year,school):
        super().__init__(name,Id,age)
        self.year=year
        self.school=school

    def __str__(self):
        return super().__str__() + f"\nyear: {self.year}\nschool: {self.school}"

class staff(member):
    def __init__(self,name,Id,age,role):
        super().__init__(name,Id,age)
        self.role=role
    def __str__(self):
        return super().__str__() + f"\nrole: {self.role}"

class faculty(staff):
    def __init__(self,name,Id,age,role,subject):
        super().__init__(name,Id,age,role)
        self.subject=subject
    def __str__(self):
        return super().__str__() + f"\nsubject: {self.subject}"

student_1=student("abc",1234,18,"1st","scds")
print(student_1)
print("\n")

staff_1=staff("xyz",4321,45,"manager")
print(staff_1)
print("\n")

faculty_1=faculty("pqr",111,25,"asst.prof","data structure")
print(faculty_1)
print("\n")