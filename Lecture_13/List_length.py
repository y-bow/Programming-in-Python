#Create a length function that takes either string or list as an input and return the length of the it.
l1 = [1,2,3]
def length(n):
    if isinstance(n, str):
        count = 0
        for i in l1:
            count+=1
        return f"Length of the string is {count}"
    elif isinstance(n,list):
        count = 0
        for i in l1:
            count+=1
        return f"Length of the list is {count}"
    else:
        print(f"Wrong Data structure")

print(length(l1))