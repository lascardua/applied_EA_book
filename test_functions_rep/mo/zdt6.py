import numpy as np
# -----------------------------------------------
#  ZDT6 Benchmark Function
# The Pareto-optimal front is formed with g(x) = 1
# -----------------------------------------------
def zdt6(x):
    n_dim = len(x)

    if any(x<0) or any(x>1):
        print('ZDT6 error -> x must be in [0,1]')
        exit(0)



    f1 = 1 - np.exp(-4*x[0])*(np.sin(6*np.pi*x[0])**6)  # objective 1
    g = 1 + 9 * (np.sum(x[1:n_dim]) / (n_dim-1))**0.25
    h = 1 - (f1 / g)**2
    f2 = g * h  # objective 2

    return np.array([f1, f2])