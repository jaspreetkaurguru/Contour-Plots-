# 3. To plot the surface curve of the function f(x,y) = x ** 3 - y  when value of z = [1,6]

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3, 21)
y = np.linspace(-3,3, 21)
x, y = np.meshgrid(x, y)
z = x ** 3 - y
levels = np.array([1, 6])
cs = plt.contour(x, y, z, levels)
cs1 = plt.contourf(x, y, z,levels)
plt.clabel(cs,inline=1,fontsize=9, colors = 'red')
plt.grid(True)
plt.axis('scaled')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Surface curve of the function f(x,y) =x**3-y')
plt.show()
