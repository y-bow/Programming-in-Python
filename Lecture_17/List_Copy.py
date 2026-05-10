l = ["Red", "Orange", "Brown"]
l1 = l[:] #Call by reference takes place
l1.append("Violet") #So, "Violet" will be updated to l1 list only
print(l)
print(l1)