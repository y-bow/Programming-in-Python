s = set()
s1 = {0}
l = [9,5,1,7,2,4,3,6]
for i in l:
    s.add(i)
print(type(s))
print(type(s1))

#How to print the set and convert it to a list
print(s)
l = list(s)
print(l)

#How to remove a element in set
s.remove(5)
print(s)

#How to pop a element
s.pop()
print(s)