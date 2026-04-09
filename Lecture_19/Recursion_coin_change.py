def coin_change(amount, coin):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if coin == 0:
        return 0
    if coin == 5:
        return coin_change(amount - 5, 5) + coin_change(amount, 2)
    elif coin == 2:
        return coin_change(amount - 2, 2) + coin_change(amount, 1)
    else:
        return coin_change(amount - 1, 1)

amount = int(input("Enter the amount : "))
print(f"Number of ways to calculate {amount} is {coin_change(amount, 5)}")