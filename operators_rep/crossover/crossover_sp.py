# -------------------------------------------------------------
#               Single Point crossover
# -------------------------------------------------------------
# Inputs
#   parent1_chrom   - first parent
#   parent2_chrom   - second parent
#   pc              - crossover probability
# Outputs:
#   child1          - first offspring
#   child2          - second offspring
# -------------------------------------------------------------
# file: crossover_sp.py
# -------------------------------------------------------------
import numpy as np
def crossover_sp(parent1_chrom, parent2_chrom, pc):
    # Compute the number of genes of the chromosomes
    num_genes = np.size(parent1_chrom)
    # Compute the crossover point
    high = num_genes - 1 # excludes the last bit
    low = 1              # excludes the first bit
    # random integers from low (inclusive) to high (exclusive).
    cross_pt = np.random.randint(low,high+1) # Note that Python
                                             # indexing starts
                                             # in 0
    # Fist child
    part1 = parent1_chrom[0:cross_pt]
    part2 = parent2_chrom[cross_pt: num_genes]
    child1 = np.concatenate((part1, part2))
    # Second child
    part1 = parent2_chrom[0:cross_pt]
    part2 = parent1_chrom[cross_pt: num_genes]
    child2 = np.concatenate((part1, part2))
    # Decide if recombined children make it to the next
    # generation
    R1 = np.random.uniform()
    if R1 > pc:
        child1 = parent1_chrom  # do not recombinate
    R2 = np.random.uniform()
    if R2 > pc:
        child2 = parent2_chrom # do not recombinate
    # Return the offspring
    return child1, child2