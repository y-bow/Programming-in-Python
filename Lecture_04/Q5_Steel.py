hard = int(input("Enter the hard of the steel : "))
carbon = float(input("Enter the carbon content of the steel : "))
tens = int(input("Enter the tensile strength of the steel : "))
if hard > 50 and carbon < 0.7 and tens > 5600:
    print("Grade 10 Steel")
elif hard > 50 and carbon < 0.7:
    print("Grade 9 Steel")
elif carbon < 0.7 and tens > 5600:
    print("Grade 8 Steel")
elif hard > 50 and tens > 5600:
    print("Grade 7 Steel")
elif hard > 50 or carbon < 0.7 or tens > 5600:
    print("Grade 6 Steel")
else:
    print("Grade 5 Steel")