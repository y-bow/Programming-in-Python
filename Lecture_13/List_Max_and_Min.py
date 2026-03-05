l1 = list(map(int,input("Enter the numbers to put in list (seperated by a space) : ").split()))
minimum = l1[0]
maximum = l1[1]
for i in range(0, len(l1)):

    if l1[i] < minimum:
        minimum = l1[i]

    if l1[i] > maximum:
        maximum = l1[i]

print(f"\nMinimum of the list is {minimum}")
print(f"\nMaximum of the list is {maximum}\n")