import numpy as np
# -----------------------------------------------
#  The ZDT2 Benchmark Function
# It is non-convex
# -----------------------------------------------
def zdt2(x):
    n_dim = len(x)

    if any(x<0) or any(x>1):
        print('ZDT2 error -> x must be in [0,1]')
        exit(0)

    f1 = x[0]  # objective 1
    g = 1 + 9 * np.sum(x[1:n_dim]) / (n_dim-1)
    h = 1 - (x[0] / g)**2
    f2 = g * h  # objective 2

    return np.array([f1, f2])