# -------------------------------------------------------------
#            Random Resetting Mutation
# -------------------------------------------------------------
# Inputs:
#    x     - n-dimensional individual to be mutated
#    v     - vector of permissible values for the genes
#    pm    - probability that a gene will undergo mutation
# Outputs:
#    mutated_x - mutated individual
# -------------------------------------------------------------
# file: mutation_rand_reset_int.py
# -------------------------------------------------------------
import numpy as np
# -------------------------------------------------------------
def mutation_rand_reset(x,v, pm):
    # No mutation is performed
    if pm == 0:
        return x
    # Create the mutated individual
    mutated_x = np.copy(x)
    # Dimensionality
    numVar = len(x)
    # Random changes
    for ll in range(numVar):
        if np.random.rand() < pm:
            mutated_x[ll] = np.random.choice(v)
    # return the mutated individual
    return mutated_x