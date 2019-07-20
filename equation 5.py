# 1. Implement the following equation 4*(x**2)+y**2 when value of z = [0,1,3,5]

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 21)
y = np.linspace(-10, 10, 21)
x,y=np.meshgrid(x,y)
z=4*(x**2)+y**2
levels=np.array([0,1,3,5])
cs=plt.contour(x,y,z,levels)
cs1 = plt.contourf(x, y, z,levels)
plt.clabel(cs,inline=20,fontsize=6)
plt.grid(True)
plt.axis('scaled')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Level curves of the function f(x,y) =4*(x**2)+y**2')
plt.show()