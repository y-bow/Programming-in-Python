arith = input("Enter the arithmetic operator ( + , - , * , / ) : ")
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if arith == '+':
    print(f"The addition of the two numbers is {a + b}")
elif arith == '-':
    print(f"The subtraction of the two numbers is {a - b}")
elif arith == '*':
    print(f"The multiplication of the two numbers is {a * b}")
elif arith == '/':
    print(f"The division of the two numbers is {a / b}")
else:
    print("Invalid operator")