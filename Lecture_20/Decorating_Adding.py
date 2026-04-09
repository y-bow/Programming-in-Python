def decorator1(add):
    def wrapper(a,b):
        print(f"\nStarted adding {a} and {b}")
        add(a,b)
        print(f"Finished adding {a} and {b}\n")
    return wrapper

@decorator1

def add(a,b):
    print(f"The sum is {a + b}")

a = int(input("Enter the value of 'a' : "))
b = int(input("Enter the value of 'b' : "))
add(a,b)