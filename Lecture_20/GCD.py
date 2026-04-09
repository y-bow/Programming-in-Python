def gcd(a, b):
    if b == 0:
        return 0
    else:
        return gcd(a % b, a)

a = int(input("Enter a number (a) : "))
b = int(input("Enter a number (b) : "))
print(f"GCD between {a} and {b} is {gcd(a, b)}")