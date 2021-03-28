# --------------------------------------------------
#                Sphere
# Implements the n-dimensional sphere function
# --------------------------------------------------
# file: sphere.py
# --------------------------------------------------
def sphere(x):
    d = len(x)
    y = 0
    for ii in range(d):
        y = y + x[ii]**2
    return y





