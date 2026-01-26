r = int(input("Enter the radius of the circle : "))
if r < 0:
    print("Radius cannot be negative")
else:
    area = 3.14*r*r
    print(f"The area of the circle is {area} cm square")