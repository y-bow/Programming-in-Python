def coin_change(amount, coin):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if coin < 0:
        return 0
    if coin == 5:
        return coin_change(amount - 5, 5) + coin_change(amount, 2)
    elif coin == 2:
        return coin_change(amount - 2, 2) + coin_change(amount, 1)
    elif coin == 1:
        return coin_change(amount - 1, 1)
    return 0

amount = 4
print(coin_change(amount, 5))
#NOT COMPLETED YET