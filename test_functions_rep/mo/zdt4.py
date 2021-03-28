import numpy as np
# -----------------------------------------------
#  ZDT4 Benchmark Function
# The Pareto-optimal front is formed with g(x) = 1
# -----------------------------------------------
def zdt4(x):
    n_dim = len(x)

    if x[0]<0 or x[0]>1:
        print('ZDT4 error -> x[0] must be in [0,1]')
        exit(0)

    if any(x[1:n_dim]<-5) or any(x[1:n_dim]>5):
        print('ZDT4 error -> x[1:end] must be in [-5,5]')
        exit(0)


    f1 = x[0]  # objective 1
    g = 1 + 10*(n_dim - 1) + np.sum(x[1:n_dim]**2 - 10*np.cos(4*np.pi*x[1:n_dim]))
    h = 1 - np.sqrt(f1 / g)
    f2 = g * h  # objective 2

    return np.array([f1, f2])