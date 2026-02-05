a = int(input("Enter the range : "))

for i in range (0 , a):
    if i % 2 == 0 or i % 3 == 0:
        print(i, end = " ")
