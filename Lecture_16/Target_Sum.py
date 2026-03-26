def sum_target(l, s):
    listlen = len(l)
    l1 = []
    for i in range(0, listlen):
        for j in range(i + 1, listlen):
            if l[i] + l[j] == s:
                print(f"{l[i],l[j]}", end = " ")
            else:
                continue

#2nd Way of Approaching target sum (Same efficiency)(Doesn't work if the target sum is 4)
def sum_target2(l, s):
    res = []
    for i in l:
        if s-i in l:
            res.append((i, s-i))
    print(res)

l = list(map(int,input("Enter the numbers to put in list (seperated by a space) : ").split()))
s = int(input("Enter the target sum : "))
sum_target(l, s)
print("\n")
sum_target2(l, s)

