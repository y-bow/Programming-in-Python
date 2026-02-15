def count(a):
    count = 0
    while a > 0:
        a = a // 10
        count += 1
    print(f"Count of the digits in the number is : {count}")

a = int(input("Enter an integer : "))
count(a)