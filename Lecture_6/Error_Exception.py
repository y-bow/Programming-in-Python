a = int(input("Enter an integer : "))
b = int(input("Enter an integer : "))

try:
    print(a/b)
except ZeroDivisionError:
    print("You divided by zero")
    
print("Mourya's laptop is dead")