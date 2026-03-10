s1 = input("Enter a string : ") #Input = aabbbcccdddd
d2 = {}
least_occured = s1[1]
most_occured = s1[0]
for i in s1:
    if i not in d2.keys():
        d2[i] = 1
    else:
        d2[i] += i
    if d2[most_occured] < d2[i]:
        most_occured = i
    elif d2[least_occured] > d2[i]:
        least_occured = i

print(f"Most occurred is : {most_occured}")
print(f"Least occurred is : {least_occured}")


