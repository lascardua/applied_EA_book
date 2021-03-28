import numpy as np
# -----------------------------------------------
#  ZDT3 Benchmark Function
# The Pareto-optimal front is formed with g(x) = 1
# -----------------------------------------------
def zdt3(x):
    n_dim = len(x)

    if any(x<0) or any(x>1):
        print('ZDT3 error -> x must be in [0,1]')
        exit(0)

    f1 = x[0]  # objective 1
    g = 1 + 9 * np.sum(x[1:n_dim]) / (n_dim-1)
    h = 1 - np.sqrt(f1 / g) - (f1/g)*np.sin(10*np.pi*f1)
    f2 = g * h  # objective 2

    return np.array([f1, f2])