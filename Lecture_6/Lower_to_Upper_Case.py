s = input("Enter a string in lower case :  ") #hello
s1=""
for i in s:
    if ord(i) <= ord('z') and ord(i) >= ord('a'):
        s1 = s1 + chr(ord(i) - 32)
    else:
        s1 = s1 + i
print(f"The given string in uppercase {s1}")