# --------------------------------------------------------------
# SBX: Simulated Binary Crossover
# --------------------------------------------------------------
# Inputs:
#   p1 - first parent
#   p2 - second parent
#   pc - crossover probability
#   eta - distribution index
# Outputs:
#   c1 - first offspring
#   c2 - second offspring
# --------------------------------------------------------------
# file: crossover_rv_sbx.py
# --------------------------------------------------------------
import numpy as np
import random
# --------------------------------------------------------------
def sbx_crossover(p1,p2, pc,eta=2):
    # number of elements of the parents
    n_dim = len(p1)
    # perform crossover ?
    if np.random.rand() < pc:
        # storage for the offspring
        c1 = np.zeros(n_dim)
        c2 = np.zeros(n_dim)

        for i in range(n_dim):
            # SBX crossover
            u = random.random()
            if u <= 0.5:
                 beta = 2. * u
            else:
                 beta = 1. / (2. * (1. - u))
            beta = beta**(1. / (eta + 1.))
            # new offspring
            c1[i] = 0.5 * (((1 + beta) * p1[i]) +
                            ((1 - beta) * p2[i]))
            c2[i] = 0.5 * (((1 - beta) * p1[i]) +
                            ((1 + beta) * p2[i]))
    else:
        # no crossover
        c1 = p1
        c2 = p2
    return c1,c2


