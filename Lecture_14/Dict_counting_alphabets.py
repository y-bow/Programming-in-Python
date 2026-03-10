s1 = input("Enter a string : ") #Input = aabbbcccdddd
d2 = {}
for i in s1:
    if i not in d2.keys():
        d2[i] = 1
    else:
        d2[i] += 1

print(d2)