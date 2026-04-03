#List Comprehension

l = [i for i in range(1,11)]
print(l)
l1 = [i*i for i in range(1,6)]
print(l1)
l2 = [chr(i) for i in range(65, 91)]
print(l2)
s = "SaiUniversity"
l3 = [i for i in s]
print(l3)
l4 = [i for i in range(1,20) if i%2==0]
print(l4)