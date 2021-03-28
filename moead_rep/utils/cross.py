# -----------------------------------------------------
# Produces a single child by crossover
# -----------------------------------------------------
# p1    - first parent
# p2    - second parent
# lb    - lower bound
# ub    - upper bound
# -----------------------------------------------------
import numpy as np
# -----------------------------------------------------
def cross(p1, p2, lb, ub):
    gamma = 0.5
    # draw a vector of len(p1) uniformly distributed
    # samples from [-gamma, 1 + gamma]
    alpha = np.random.uniform(-gamma, 1 + gamma, len(p1))
    # blend the two parents, using as weights vector alpha
    y = alpha * p1 + (1 - alpha) * p2
    # enforce the boundaries of the search space
    y = np.minimum(np.maximum(y, lb), ub)
    # return the result of the crossover
    return y