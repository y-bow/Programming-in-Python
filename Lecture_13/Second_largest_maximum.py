l1 = list(map(int,input("Enter the numbers to put in list (seperated by a space) : ").split()))
maximum = l1[0]
maximumtwo = l1[1] if len(l1) > 1 else float('-inf')

for i in range(1, len(l1)):
    if l1[i] > maximum:
        maximumtwo = maximum  # Old max becomes second max
        maximum = l1[i]
    elif l1[i] > maximumtwo:
        maximumtwo = l1[i]

print(f"\nMaximum of the list is {maximum}\n")
print(f"Second largest is {maximumtwo}")