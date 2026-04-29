import matplotlib.pyplot as plt
import numpy as np

#From matplotlib import pyplot as plt

x = np.array([1,2,3,4,5])
x1 = np.linspace(0,5,50)
x2 = np.linspace(0,5,50)
y = x**2
y1 = x1**2
y2 = x2**3
print(y)
fig,ax = plt.subplots(figsize = (10,8),layout = "constrained")
ax.plot(x,y,label = "y = x ^ 2")
ax.plot(x1,y1,label = "With more Points")
ax.plot(x2,y2,label = "y = x ^ 3")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_title("Simple Graph: ")
ax.grid()
ax.legend()
plt.show()