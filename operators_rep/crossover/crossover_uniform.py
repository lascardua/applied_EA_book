# -------------------------------------------------------------
#              Uniform crossover
# -------------------------------------------------------------
# Inputs:
#   parent1_chrom   - first parent
#   parent2_chrom   - second parent
#   pc              - crossover probability
# Outputs:
#   child1          - first offspring
#   child2          - second offspring
# -------------------------------------------------------------
# file: crossover_uniform.py
# -------------------------------------------------------------
import numpy as np
# -------------------------------------------------------------
def crossover_uniform(parent1_chrom, parent2_chrom, pc):
    # Number of genes of each parent
    num_genes = np.size(parent1_chrom)
    # Declare variables for the children
    child1 = np.zeros(num_genes)
    child2 = np.zeros(num_genes)
    # uniform recombination
    for ii in range(num_genes):
        r = np.random.uniform()
        # There is a 50% chance that a feature comes
        # from a given parent
        if r < 0.5:
            child1[ii] =  parent1_chrom[ii]
            child2[ii] = parent2_chrom[ii]
        else:
            child1[ii] =  parent2_chrom[ii]
            child2[ii] = parent1_chrom[ii]
    # Decide if recombined children make it to the
    # next generation
    R1 = np.random.uniform(low=0.0, high=1.0)
    if R1 >= pc:
        child1 = parent1_chrom  # do not recombinate
    R2 = np.random.uniform()
    if R2 >= pc:
        child2 = parent2_chrom # do not recombinate
    # Return the offspring
    return child1, child2