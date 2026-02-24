#Swapping with temp variable *XOR

a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))

print(f"\n{a} is the 'a' value and {b} is the 'b' value before swapping")
a = a^b
b = a^b
a = a^b
print(f"{a} is the 'a' value and {b} is the 'b' value after swapping\n")