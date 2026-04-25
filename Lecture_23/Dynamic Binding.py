#Dynamic Binding

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

def animal_sound(animals):
    animals.sound()

d1 = Dog()
# d1.sound()
c1 = Cat()
# c1.sound()
a1 = Animal()

animal_sound(d1)
animal_sound(c1)
animal_sound(a1)

# "print" is a example of Polymorphism   
# Abstraction is the process of removing specific details to focus on essential characteristics, creating a general concept or model