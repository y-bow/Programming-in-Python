a = int(input("Enter a number : "))
if a & 1 == 0:
    print(f"Remainder is 0 and quotient is {a>>1}")
else:
    print(f"Remainder is {a & 1} and quotient is {a>>1}")
    