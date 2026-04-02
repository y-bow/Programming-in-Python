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
    def __gt__(self, other_object): # Giving new meaning for this greater than symbol, it is not gonna work for structures. The process of giving new meaning is called "overloading".
        return self.__age > other_object.__age

p1 = person("Robert", 25, "M", 145)
p1.person_details()
p2 = person("Alice", 30, "F", 140)
print(p1 > p2)
