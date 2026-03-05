l1 = list(map(int,input("Enter the numbers to put in list (seperated by a space) : ").split()))
maximum = l1[1]
for i in range(0, len(l1)):
    
    temp = l1[i]
    if l1[i] > maximum:
        maximum = l1[i]
    if temp < maximum:
        maximumtwo = temp

print(f"\nMaximum of the list is {maximum}\n")
print(maximumtwo)

#1 for loop, no sorting, second largest number