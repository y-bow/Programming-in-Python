l1 = ["my_name", 18, "SCDS", [2,3,4,5]]
print(l1[0]) 
print(l1[0][0])
print(l1[0][1])

for i in range(len(l1[0])):
    print(l1[0][i], end = ", ")

for i in range(len(l1[3])):
    print(l1[3][i], end = ", ")