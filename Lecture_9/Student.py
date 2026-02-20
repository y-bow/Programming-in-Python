class student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
    def student_details(self):
        print(f"Name : {self.name} | ID : {self.id} | CGPA : {self.cgpa}")
    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa
    def update_name(self, new_name):
        self.name = new_name

s1 = student("Student1", 1, 7.5)
s2 = student("Student2", 2, 8.0)
s1.student_details()
s2.student_details()
s2.update_cgpa(9.0)
s2.student_details()
s1.update_name("Student3")
s1.student_details()