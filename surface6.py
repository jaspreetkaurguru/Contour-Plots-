# 6. To plot the surface curve of the function f(x,y) =2-x-y when value of z = [-6,-4,-2,0,2,4,6]

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 21)
y = np.linspace(-10, 10, 21)
x,y=np.meshgrid(x,y)
z=2-x-y
levels=np.array([-6,-4,-2,0,2,4,6])
cs=plt.contour(x,y,z,levels)
cs1 = plt.contourf(x, y, z,levels)
plt.clabel(cs,inline=1,fontsize=9, colors = 'red')
plt.grid(True)
plt.axis('scaled')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('surface curve of the function f(x,y) =2-x-y')
plt.show()