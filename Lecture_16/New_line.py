with open("Text.txt","r") as f:
    data = f.read()

count = 0
for i in data:
    if i == "\n":
        count+=1

print(count)