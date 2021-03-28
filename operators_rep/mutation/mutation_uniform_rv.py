# -------------------------------------------------------------
#                 Uniform Mutation
# Analogous to the binary (bit flipping) mutation and random
# resetting mutation
# -------------------------------------------------------------
# Inputs:
#   x  - n-dimensional individual to be mutated
#   pm - probability that a gene will undergo mutation
#   a  - lower bound for the values of the genes
#   b  - upper bound for the values of the genes
# Output:
#   mutated_x - mutated individual
# -------------------------------------------------------------
# file: mutation_uniform_rv.py
# -------------------------------------------------------------
import numpy as np
# -------------------------------------------------------------
def mutation_uniform_rv(x, pm, a, b):
    # No mutation is performed
    if pm == 0:
        return x
    # Number of genes of the individual
    num_genes = np.size(x)
    # Create the mutated individual
    mutated_x = np.copy(x)
    # Uniform mutation
    for k in range(num_genes):
        # Generate a random number
        r = np.random.uniform()
        # Mutate this gene?
        if r < pm:
            # Generate a uniformly distributed random
            # number in [a,b]
            mutated_x[k] = np.random.uniform(a[k],b[k],1)
    # Return the mutated chromosome
    return mutated_x

