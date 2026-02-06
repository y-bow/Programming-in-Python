a = int(input("Enter a number : "))
squares = 0
while a > 0:
    lastdigit = a % 10
    v = lastdigit*lastdigit
    squares += v
    a = a // 10
print(f"squares of the digits in the number is : {squares}")