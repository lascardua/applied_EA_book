
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization!
from test_functions_rep.so.sphere import sphere


x = np.linspace(-6, 6, 500)
y = np.linspace(-6, 6, 500)

X, Y = np.meshgrid(x, y)

Z = np.zeros((len(x),len(y)))
for ix in range(len(x)):
    for iy in range(len(y)):
        Z[ix,iy] = sphere([X[ix, iy], Y[ix, iy]])


fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color='gray')
ax.plot_surface(X, Y, Z, cmap = plt.cm.gray)
# surf = ax.plot_wireframe(X, Y, Z, color='gray')
ax.contour(X, Y, Z, 50, cmap="gray", linestyles="solid", offset=-1)
ax.contour(X, Y, Z, 50, colors="k", linestyles="solid")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('2D Sphere function')



plt.show()