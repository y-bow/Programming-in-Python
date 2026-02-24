a = float(input("Enter the cost of the item : "))
b = float(input("Enter the selling price of the item : "))
if a > b:
    print(f"The item is in sale and it is a profit of {a - b}")
else:
    print(f"The item is not in sale and it is a loss of {b - a}")