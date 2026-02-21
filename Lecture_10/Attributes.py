#Attributes (Using (example : p1, p2) to introduce a function (example : update, in this code))

class person:
    def __init__(self, name, age, gender, height):
        self.__name = name #
        self.__age = age
        self.__gender = gender
        self.__height = height
    def __str__(self):
        return(f"Name : {self.__name} \nAge : {self.__age} \nGender : {self.__gender} \nHeight : {self.__height} ")
    def update(self, Age = None, Height = None):
        if Age is not None:
            self.__age = Age
        if Height is not None:
            self.__height = Height

print("\n")
p1 = person("Person_1", 18, "M", 180)
print(p1)
p1.update(Age = 50, Height = 190)
print("\n")