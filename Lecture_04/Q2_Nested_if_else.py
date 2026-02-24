n1 = int(input("Enter a natural number (n1) : "))
o1 = input("Enter an operator (o1) [+, -, *]: ")
n2 = int(input("Enter a natural number (n2) : "))
o2 = input("Enter an operator (o2) [+, -, *]: ")
n3 = int(input("Enter a natural number (n3) : "))


if o1 == "+":
    temp = n1 + n2
elif o1 == "-":
    temp = n1 - n2
elif o1 == "*":
    temp = n1 * n2
else:
    print("Invalid operator")
    exit() #To break out of the Function when we get a invalid operator

if o2 == "+":
    print(f"Answer for operation : {temp + n3}")
elif o2 == "-":
    print(f"Answer for operation : {temp - n3}")
elif o2 == "*":
    print(f"Answer for operation : {temp * n3}")
else:
    print("Invalid operator")
    exit()