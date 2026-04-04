try:
    n = int(input("Enter Index:"))
    s = "abcd"
    c = s[n]
except IndexError:
    print("Index out of bounds")
else:
    print(c)
finally:
    print("Execution completed")