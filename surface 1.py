# 1. To plot the surface curve of the function f(x,y) = 10-x2-y2  when value of z = [1,6,9]

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,10)
y = np.linspace(-4,4,10)
x,y=np.meshgrid(x,y)
z=10-x**2-y**2
levels=np.array([1,6,9])
cs=plt.contour(x,y,z,levels)
cs1=plt.contourf(x,y,z,levels)
plt.clabel(cs,inline=1,fontsize=9, colors = 'red')
plt.grid(True)
plt.axis('scaled')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Surface curve of the function f(x,y) =10-x**2-y**2')
plt.show()