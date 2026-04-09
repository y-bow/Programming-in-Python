def added(*args):
    total = 0
    for i in args:
        total = total + i
    return (total)

print(added(12, 45, 54, 5, 43))
#print(added('p', 'y', 't', 'h', 'o', 'n')) #It won't work
print(added(1.2, 4.5, 5.4, 5, 4.3))