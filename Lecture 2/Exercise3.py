a = int(input("Enter the length of the rectangle : "))
b = int(input("Enter the breadth of the rectangle : "))

if a < 0:
    print("Invalid integer")
elif b < 0:
    print("Invalid integer")
else:
    print(f"The area of the rectangle is {a * b}")
    print(f"The perimeter of the rectangle is {2*(a + b)}")