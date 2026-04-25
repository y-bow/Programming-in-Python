#Static Binding

def add(a,b):
    return a+b

def add(a,b,c):
    return a+b+c

print(add(2,4)) #Wont work, Function Overloading
print(add(1,3,5))