a = int(input("Enter an integer : "))
if a % 5 == 0:
    print("The integer is divisible by 5")
    if a % 7 == 0:
        print("The integer is divisible by 7")
    else:
        print("The integer is not divisible by 7")
else:
    print("The integer is not divisible by 5")
    if a % 7 == 0:
        print("The integer is divisible by 7")
    else:
        print("The integer is not divisible by 7")