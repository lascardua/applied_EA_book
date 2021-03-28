# --------------------------------------------------
#                Griewank
# Implements the n-dimensional griewank function
# --------------------------------------------------
# file: griewank.py
# --------------------------------------------------
import numpy as np
# --------------------------------------------------
def griewank(xx):
    d = len(xx)
    sum = 0
    prod = 1

    for ii in range(d):
        xi = xx[ii]
        sum = sum + xi**2/4000
        prod = prod * np.cos(xi/np.sqrt(ii + 1))
    y = sum - prod + 1
    return y
