import math

try:
    a = int(input("Enter an integer : "))
    
    if a < 0:
        print(math.sqrt(abs(a)))
    else:
        print(math.sqrt(a))

except ValueError:
    print("Invalid input")

finally:
    print("Execution completed")