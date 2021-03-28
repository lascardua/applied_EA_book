
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #<-- Note the capitalization!
from test_functions_rep.so.griewank import griewank


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = np.zeros((len(x),len(y)))

for ix in range(len(x)):
    for iy in range(len(y)):
        Z[ix,iy] = griewank([X[ix, iy], Y[ix, iy]])


fig = plt.figure()
fig.set_tight_layout(True)
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color = 'gray')
ax.plot_surface(X, Y, Z, cmap = plt.cm.gray)


ax.contour(X, Y, Z, 5, cmap="gray", linestyles="solid", offset=-1)
ax.contour(X, Y, Z, 5, colors="k", linestyles="solid")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('2D Griewank function')


plt.show()