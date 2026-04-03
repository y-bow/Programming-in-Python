t = (5,3,4,1,2,6)
l = list(t)
n = len(l)
for i in range(0, n-1):
    for j in range(0, n-1-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(f"\nSorted Array : \n")
t = tuple(l)
print(t)
