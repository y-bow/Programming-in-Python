a = int(input("Enter an integer : "))
if a % 2 == 0:
    print("The integer is divisible by 2")
elif a % 3 == 0:
    print("The integer is divisible by 3")
elif a % 5 == 0:
    print("The integer is divisible by 5")
elif a % 7 == 0:
    print("The integer is divisible by 7")
else:
    print("Not divisible by anything")