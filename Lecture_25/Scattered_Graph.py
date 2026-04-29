from matplotlib import pyplot as plt
import numpy as np
a = np.random.uniform(-1, 1, 5)
b = np.random.uniform(-1, 1, 5)

fig,ax = plt.subplots(figsize = (10,7),layout ='constrained')
ax.scatter(a,b,s = 50)
ax.plot(a,b)
ax.grid()
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_title("Scattered Diagram")
plt.show()