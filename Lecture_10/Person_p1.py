class person:
    def __init__(self, name, age, gender, height):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__height = height
    def person_details(self):
        print(f"Name : {self.__name} | Age : {self.__age} | Gender : {self.__gender} | Height : {self.__height} ")
    def update(self, new_age, new_height):
        self.__age = new_age
        self.__height = new_height
    def compare(self, others):
        if self.__age > others.__age:
            print(f"{p1.__name} is older than {p2.__name}")
        else:
            print(f"{p2.__name} is older than {p1.__name}")

p1 = person("Robert", 25, "M", 145)
p2 = person("Alice", 30, "F", 140)
p1.person_details()
p1.compare(p2)