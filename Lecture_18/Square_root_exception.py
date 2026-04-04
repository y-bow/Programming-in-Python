import math
try:
    a = int(input("Enter an integer : "))
    c = math.sqrt(a)
except ValueError:
    p = abs(a)
    print(math.sqrt(p))
else:
    print(c)
finally:
    print("Execution Completed")