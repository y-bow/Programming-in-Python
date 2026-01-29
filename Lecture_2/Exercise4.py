# <=0 real
print("Expression : a*x*x + bx + c = 0")
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
d = b*b - 4*a*c
e = (-b + d**0.5)/2*a
f = (-b - d**0.5)/2*a
if d >= 0:
    print("Real roots")
    print(f"The solution 1 is {e}")
    print(f"The solution 2 is {f}")
else:
    print("Complex roots")