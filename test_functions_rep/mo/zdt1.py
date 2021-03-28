# -----------------------------------------------
#  ZDT1 Benchmark Function
# The Pareto-optimal front is formed with g(x) = 1
# -----------------------------------------------
import numpy as np
# -----------------------------------------------
def zdt1(x):
    n_dim = len(x)
    f1 = x[0]  # objective 1
    g = 1 + 9 * np.sum(x[1:n_dim]) / (n_dim-1)
    h = 1 - np.sqrt(f1 / g)
    f2 = g * h  # objective 2
    return np.array([f1, f2])