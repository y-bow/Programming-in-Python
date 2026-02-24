a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))

try:
    print(a/b)
except ZeroDivisionError:
    print("You divided by zero")
