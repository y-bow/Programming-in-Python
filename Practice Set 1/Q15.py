print("Please enter your choice")
print("1. Check your balance")
print("2. View Offers")
print("3. Special Recharge")
print("Enter 0 to exit\n")
a = int(input("Your Choice : "))
if a == 1:
    print("\nYour balance is 45600000000 ₩\n")
elif a == 2:
    print("\n[You can play a game to double your money]")
    print("[You can buy a BMW M5 now with your credit score]\n")
elif a == 3:
    b = int(input("\nEnter your recharge amount : "))
    print(f"{b} ₩ amount of cash has been recharged\n")
elif a == 0:
    print("\nThank you for using\n")
else:
    print("\nInvalid choice\n")