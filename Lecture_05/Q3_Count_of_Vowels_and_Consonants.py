s = "Sai University"
v = 0
c = 0
for i in range (0 , 14 , 1):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
        v+=1
    elif s[i] != " ":
        c+=1
print(f"Count of Vowels in the string {s} is {v}")
print(f"Count of consonants in the string {s} is {c}")