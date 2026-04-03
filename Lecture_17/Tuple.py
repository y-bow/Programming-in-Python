#Tuple Comprehension

t = (1,2,3,4,5,6)
print(t)
# t[1] = 3 # --> Gives error because tuple is immutable (It cannot be changed after declaration)
# print(t)
t1 = t[1:4] # --> Starts printing from 1st index and stops at 4th index
t2 = t[::-1] # --> Reverses the tuple
print(t1)
print(t2)

#How to append something to a tuple :-

l = list(t) #Converts all the elements of the tuple to a list
print(l)
l[1] = 13 #Changes the value at index 1 to be 13
print(l)
t = tuple(l) #Converts all the elements of the changed list back to a tuple
print(t)