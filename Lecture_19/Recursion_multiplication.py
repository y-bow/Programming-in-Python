def mult(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return a + mult(a, b - 1)

a = int(input("Enter a number (a) : "))
b = int(input("Enter a number (b) : "))
print(f"Multiplication between {a} and {b} is {mult(a, b)}")