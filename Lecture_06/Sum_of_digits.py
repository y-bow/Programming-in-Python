a = int(input("Enter a number : "))
sum = 0
while a > 0:
    lastdigit = a % 10
    sum += lastdigit
    a = a // 10
print(f"sum of the digits in the number is : {sum}")