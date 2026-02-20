class person:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
    def person_details(self):
        print(f"Name : {self.name} | Age : {self.age} | Gender : {self.gender} | Height : {self.height} ")
    def update(self, new_age, new_height):
        self.age = new_age
        self.height = new_height

p1 = person("Person1", 18, "M", 180)
p1.person_details()
p1.update(20, 185)
p1.person_details()