a = int(input("Enter the range : "))

for i in range (0 , a):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end = " ")
