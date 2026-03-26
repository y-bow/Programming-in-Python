with open("Text.txt","r") as f:
    data = f.read()
    #data = f.readline() ---> Gives the first line of the text file.
    #data = f.readlines() ---> Gives all the lines of the text file.
print(data)