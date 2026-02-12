#Call by Value

def change(x):
    def g(x):
        x = "Table Tennis"
        print(x)
    g(x)
    x += 1
    return x

x = 4
print(x)
x = change(x) #if only change(X), it is only call by value
print(x)

#Tip: Change the variables of x to (z and y)