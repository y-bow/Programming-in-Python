def count(n):
    if n == 0:
        return 0
    else:
        return 1 + count(n // 10)
n = int(input("Enter a number : "))
print(f"The count of digits in the number {n} is {count(n)}")