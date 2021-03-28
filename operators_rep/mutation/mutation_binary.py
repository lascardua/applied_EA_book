# -----------------------------------------------------------
#                   Binary Mutation
# -----------------------------------------------------------
# Inputs:
#   x           - individual to undergo mutation
#   pm          - mutation probability
# Outputs:
#   mutated_x   - mutated individual
# -----------------------------------------------------------
# file: mutation_binary.py
# -----------------------------------------------------------
import numpy as np
# -----------------------------------------------------------
# Auxiliary function to flip a bit
def flip_bit(bit):
    if bit==0:
        bit = 1
    else:
        bit = 0
    return bit
# Binary mutation function
def mutation_binary(x, pm):
    # if pm=0, no mutation is performed
    if pm == 0:
        return x
    # Compute the number of genes in x
    M = np.size(x)
    # This is because in Python arguments are passed
    # by reference, not by value
    mutated_x = np.copy(x)
    # Mutate each gene
    for k in range(M):
        r = np.random.uniform()
        if r < pm:
            mutated_x[k] = flip_bit(x[k])
    # Return mutated individual
    return mutated_x

