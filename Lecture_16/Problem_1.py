#Replace Nothing with Something
text = "Problem_1.txt"

with open(text, "r") as f:
    data = f.read()

data = data.replace("nothing", "something")

with open(text, "w") as f:
    f.write(data)