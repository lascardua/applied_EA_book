# --------------------------------------------------------------
# Intermediate Crossover
# --------------------------------------------------------------
# Inputs
#   p1   - first parent
#   p2   - second parent
#   pc   - crossover probability
# Outputs:
#   child1 - first offspring
#   child2 - second offspring
# --------------------------------------------------------------
# file: crossover_rv_intermediate.py
# --------------------------------------------------------------
import numpy as np
# --------------------------------------------------------------
def intermediate_crossover(p1, p2, pc):
    n_dim = len(p1)
    # perform crossover?
    if np.random.rand() < pc:
        child1 = np.zeros(n_dim)
        child2 = np.zeros(n_dim)
        for id in range(n_dim):
            # alpha - random vector in [a,b]
            b = 1.25
            a = -0.25
            alpha = (b-a)*np.random.random_sample() + a
            # blending
            child1[id] = p1[id] * alpha * (p2[id] - p1[id])
            child2[id] = p2[id] * alpha * (p1[id] - p2[id])
    else:
        # no crossover
        child1 = p1
        child2 = p2
    return child1, child2