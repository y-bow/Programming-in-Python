y1 = float(input("\nEnter the point of y1 : "))
y2 = float(input("Enter the point of y2 : "))
y3 = float(input("Enter the point of y3 : "))
x1 = float(input("Enter the point of x1 : "))
x2 = float(input("Enter the point of x2 : "))
x3 = float(input("Enter the point of x3 : "))
slope1 = ((y2 - y1)/(x2 - x1))
slope2 = ((y3 - y2)/(x3 - x2))
if slope1 == slope2:
    print(f"\nIt is a straight line {slope1, slope2}\n")
else:
    print("\nIt is not a straight line\n")
