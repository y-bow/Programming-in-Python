s1 = input("Enter a string : ")
s2 = input("Enter a character to find in the string : ")
count = 0
for i in s1:
    if i == s2:
        count+=1
    else:
        continue
if count == 1:
    print("Character found")
else:
    print("Character not found")

