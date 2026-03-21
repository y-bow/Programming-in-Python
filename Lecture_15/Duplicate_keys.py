def seperate():
    n = input("Enter a string in lowercase letter : ")
    d1 = {}
    result = []
    word = ""
    for i in n:
        if i not in d1.keys():
            d1[i] = 1
        else:
            d1[i]+=1
    for i in d1.keys():
        for j in range(d1[i]):
            word+=i
        result.append(word)
        word = ""

    print(d1.keys())

seperate()