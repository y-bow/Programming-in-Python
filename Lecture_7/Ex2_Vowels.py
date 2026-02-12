def vowelconsonant (str):
    vo = 0
    co = 0
    vowels = "aeiouAEIOU"
    for i in str:
        if i in vowels:
            vo+=1
        else:
            co+=1
    print(f"{vo} vowels are present")
    print(f"{co} consonants are present")

str = input("Enter a string : ")
vowelconsonant(str)