l = ["Red", "Orange", "Brown"]
l1 = l[:] #Call by reference takes place
l1.append("Violet") #So, "Violet" will be uplaoded to both l and l1
print(l)
print(l1)