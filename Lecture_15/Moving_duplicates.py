
def moveDups():
    n = input("Enter a string in lowercase letter : ")
    s1 = ""
    s2 = ""
    d1 = {}
    for i in n:
        if i not in d1.keys():
            d1[i] = 1
            s1+=i
        else:
            s2+=i
        
    return s1+"_"+s2
print(moveDups())