#A random string is given, return a string without duplicate alphabets.
s1 = input("Enter a string : ")
d2 = {}
s2 = ""
for i in s1:
    if i not in d2.keys():
        d2[i] = 1
        s2 += i
    else:
        continue

print(s2)