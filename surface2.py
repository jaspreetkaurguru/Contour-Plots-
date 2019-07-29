# 2. To plot the surface curve of the function f(x,y) = x2+y2  when value of z = [1,6,9]

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,10)
y = np.linspace(-3,3,10)
x, y = np.meshgrid(x, y)
z = x ** 2 + y ** 2
levels = np.array([1, 6, 9])
cs = plt.contour(x, y, z, levels)
cs1=plt.contourf(x,y,z,levels)
plt.clabel(cs,inline=1,fontsize=9, colors = 'red')
plt.grid(True)
plt.axis('scaled')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('surface curve of the function f(x,y) =x**2+y**2.')
plt.show()
