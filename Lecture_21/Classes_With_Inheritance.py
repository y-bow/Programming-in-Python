#INHERITANCE

class animal:
    def sound(self):
        return "makes sound"
    def move(self):
        return "every animal moves"

#lower classes have more advantage is it can use many more methods from different classes

class dog(animal): #inherit the class animal
    #pass # we can use pass to move forward
    def sound_1(self):
        return "barks"
    def pet(self):
        return "it can be trained"

class cat(animal):
    def sound_2(self):
        return "meow"
        

a1=animal()
print(a1.sound())
d1=dog()
print(d1.sound_1())
print(d1.sound()) #calling the sound method from animal
print(d1.move())
c1=cat()
print(c1.sound_2(),c1.sound())