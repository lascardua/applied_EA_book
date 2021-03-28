# -------------------------------------------------------------
#            Gaussian Mutation
# -------------------------------------------------------------
# This function can be used only with real-valued representations
# -------------------------------------------------------------
# Inputs:
#   x  - n-dimensional individual to be mutated
#   pm - probability that a gene will undergo mutation
#   a  - lower bound for the values of the genes
#   b  - upper bound for the values of the genes
# Output:
#   mutated_x - mutated individual
# -------------------------------------------------------------
# file: mutation_gaussian_rv.py
# -------------------------------------------------------------
import numpy as np
def mutation_gaussian_rv(x, pm, a, b):
    # No mutation is performed
    if pm == 0:
        return x
    num_genes = np.size(x)
    # create the mutated individual
    mutated_x = np.copy(x)
    # Uniform mutation
    for k in range(num_genes):
        # Generate a random number
        r = np.random.uniform()
        # Mutate this gene?
        if r < pm:
            # mutation by adding random perturbation
            # from a Gaussian distribution with zero mean
            mutated_x[k] = \
                    0.9*mutated_x[k] + \
                    0.1*((b[k] - a[k]) * np.random.randn())
            # keep the mutated individual in [a,b]
            mutated_x[k] = np.clip(mutated_x[k],a[k],b[k])
    # Return the mutated individual
    return mutated_x

