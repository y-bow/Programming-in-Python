try:
    a = int(input("Enter an integer : "))
    b = int(input("Enter an integer : "))
    c = a // b
except ZeroDivisionError:
    print("Zero division error")
else:
    print(f"Result : {c}")
finally:
    print("Execution complete!!")