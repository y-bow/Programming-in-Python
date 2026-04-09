def count(s):
    if s == "":
        return 0
    else:
        return 1 + count(s[1:])
    
s = input("Enter a string : ")
print(f"The string {s} has {count(s)} characters")