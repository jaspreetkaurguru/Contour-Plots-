# 5. To plot the surface curve of the function f(x,y) = 4*(x**2)+y**2 when value of z = [0,1,3,5]

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,21)
y = np.linspace(-3,3,21)
x,y=np.meshgrid(x,y)
z=4*x**2+y**2
levels=np.array([0,1,3,5])
cs=plt.contour(x,y,z,levels)
cs1 = plt.contourf(x, y, z,levels)
plt.clabel(cs,inline=1,fontsize=9, colors = 'red')
plt.grid(True)
plt.axis('scaled')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('surface curve of the function f(x,y) =4*(x**2)+y**2')
plt.show()