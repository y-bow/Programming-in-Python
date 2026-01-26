a = int(input("Enter first integer : "))
b = int(input("Enter second integer : "))

if a > b:
    print(f"First integer {a} is greater than second integer{b}")
elif b > a:
    print(f"Second integer {b} is greater than first integer {a}")
else:
    print(f"Both {a} and {b} are equal")