a = int(input("Enter the integer : "))
if a & (a - 1) == 0:
    print("It is a power of 2")
else:
    print("It is not a power of 2")