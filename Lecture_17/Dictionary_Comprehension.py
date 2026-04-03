#Dictionary Comprehension

d = {i:i*i for i in range(1,9)}
print(d)
d1 = {chr(i):i for i in range(65,75)}
print(d1)
s = "ABCDEFGHIJKL"
d2 = {ord(i):i for i in s if i not in "AEIOU"}
print(d2)