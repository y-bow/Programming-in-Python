a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))
c = int(input("Enter the third integer : "))

if a <= b and a <= c:
    print(f"{a} is the minimum number")
elif b <= a and b <= c:
    print(f"{b} is the minimum number")
else:
    print(f"{c} is the minimum number")