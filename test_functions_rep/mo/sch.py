import numpy as np
# -----------------------------------------------
#  the SCH Benchmark Function
# -----------------------------------------------
def sch(x):
    n_dim = np.ndim(x)

    # x must be a scalar
    if n_dim == 1:
        x = x[0]

    if n_dim > 1:
        print('x must be a scalar')
        exit(0)

    if x<-10**3 or x>10**3:
        print('ZDT1 error -> x must be in [-10**3,10**3]')
        exit(0)

    f1 = x **2 # objective 1
    f2 = (x - 2)**2  # objective 2

    return np.array([f1, f2])