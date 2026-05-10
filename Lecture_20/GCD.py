def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter a number (a) : "))
b = int(input("Enter a number (b) : "))
print(f"GCD between {a} and {b} is {gcd(a, b)}")