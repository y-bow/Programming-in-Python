def decorator1(greet):
    def wrapper():
        print("\nStarted\n")
        greet()
        print("\nEnded\n")
    return wrapper

@decorator1

def greet():
    print("Namaskaram!")

greet()