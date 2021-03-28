# --------------------------------------------------------------
# Blending Crossover
# --------------------------------------------------------------
# Inputs
#   p1   - first parent
#   p2   - second parent
#   pc   - crossover probability
# Outputs:
#   child1 - first offspring
#   child2 - second offspring
# --------------------------------------------------------------
# file: crossover_rv_blending.py
# --------------------------------------------------------------
import numpy as np
# --------------------------------------------------------------
def blending_crossover(p1, p2, pc):
    n_dim = len(p1)
    # perform crossover?
    if np.random.rand() < pc:
        # alpha - random vector in [0,1]
        alpha = np.random.rand(n_dim)
        # blending
        child1 = alpha * p1 + (1 - alpha) * p2
        child2 = alpha * p2 + (1 - alpha) * p1
    else:
        # no crossover
        child1 = p1
        child2 = p2
    return child1, child2