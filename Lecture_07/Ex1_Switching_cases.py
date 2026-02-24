def switchcase(s):
    s1=""
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            s1 = s1 + chr(ord(i) - 32)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            s1 = s1 + chr(ord(i) + 32)
    return s1
s = input("Enter a string to switch its case : ")
s1 = switchcase(s)
print(f"The given string after switching is {s1}")