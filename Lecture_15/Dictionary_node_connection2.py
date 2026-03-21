d1 = {"A" : ["D", "E"], "B" : ["E", "C"], "C" : ["B"], "D" : ["A", "E"], "E" : ["A", "B", "D"]}
n1 = input("Enter first node : ")
n2 = input("Enter second node : ")
n3 = input("Enter third node : ")
if n1 in d1.keys():
    if n2 in d1[n1]:
        print("True, they are connected")
    else:
        if (n1 in d1[n3] and n2 in d1[n3]):
            print(f"They are connected through {n3}")
else:
    print("Invalid key")