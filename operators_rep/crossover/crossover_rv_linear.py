# --------------------------------------------------------------
# Linear Crossover
# --------------------------------------------------------------
# p1 - first parent
# p2 - second parent
# pc - crossover probability
# --------------------------------------------------------------
# file: crossover_rv_linear.py
# --------------------------------------------------------------
import numpy as np
def linear_crossover(p1, p2, pc):
    n_dim = len(p1)
    # perform crossover?
    if np.random.rand() < pc:
        # alpha - random vector in [a,b]
        b = 1.25
        a = -0.25
        alpha = (b-a)*np.random.random_sample() + a
        # blending
        child1 = p1 * alpha * (p2 - p1)
        child2 = p2 * alpha * (p1 - p2)
    else:
        # no crossover
        child1 = p1
        child2 = p2
    return child1, child2