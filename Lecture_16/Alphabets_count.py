with open("Text.txt","r") as f:
    data = f.read()

count = 0
for i in data:
    if (data[i] >= "a" and data[i] <= "z") or (data[i] >= "A" and data[i] <= "Z"):
        count+=1

print(count)