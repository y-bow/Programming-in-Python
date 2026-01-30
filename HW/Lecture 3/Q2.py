n = int(input("Enter an integer to find the binary : "))
res = ''

while n > 0:
    res = str(n & 1) + res
    n >>= 1
print(f"Binary value : {res}")