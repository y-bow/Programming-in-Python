import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a[0])
print(a[2:])
print(a[:3])

b = np.array([[12,3,4,4,5],[5,6,7,8,9],[11,12,13,14,15]])
print(b[0][3])
print(b[2][2])
print(b[1,3])

print(a.ndim)
len(a.shape)

if len(a.shape) == a.ndim:
    print("Dimension verified")
else:
    print("Dimension not verified")

c = np.array([1.2,3.0,4.4,4.1,5.2])
print(c.dtype)

zn = np.zeros(5)
print(zn)

on = np.ones(5)
print(on)

em = np.empty(2)
print(em)

ra = np.arange(10)
print(ra)

ra = np.arange(5, 15, 3)
print(ra)

va = np.linspace(0, 10, num = 10)
print(va)

x = np.array([[2,6,1],[7,1,15]])
print(x.shape)

y = np.array([[2,1,5],[1,2,3]])
z = np.concatenate((x, y), axis=1)

print(z)

vr = np.arange(5)
print(vr)
rv = np.reshape(2, 2)
print(rv)