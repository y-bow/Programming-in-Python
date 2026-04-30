from matplotlib import pyplot as plt
import numpy as np
n = int(input("Enter a number : "))
x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)
total_points = np.arange(1, n+1)

in_circle = x**2+y**2<=1
# print(in_circle)
count_cummulative = np.cumsum(in_circle)
# print(f"{count_cummulative} is the count of points in Circle")
pi_value = (count_cummulative*4)/total_points
fig,ax = plt.subplots(1,2, figsize = (12,6), layout = 'constrained')
ax[0].plot(total_points,pi_value)
ax[0].axhline(np.pi, color = 'red')
ax[0].set_title("Pi Graph")
ax[0].set_xlabel("Number of Iterations")
ax[0].set_ylabel("Pi Value")
ax[1].scatter(x[in_circle],y[in_circle])
ax[1].scatter(x[~in_circle],y[~in_circle])
circle=plt.Circle((0,0),1,fill = False)
ax[1].add_patch(circle)
plt.show()
# print(pi_value)