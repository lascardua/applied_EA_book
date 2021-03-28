# -------------------------------------------------------------
#               Double Point crossover
# -------------------------------------------------------------
# Inputs
#   parent1_chrom   - first parent
#   parent2_chrom   - second parent
#   pc              - crossover probability
# Outputs:
#   child1          - first offspring
#   child2          - second offspring
# -------------------------------------------------------------
# file: crossover_dp.py
# -------------------------------------------------------------
import numpy as np
def crossover_dp(parent1_chrom, parent2_chrom, pc):
    # Compute the range of valid crossing points
    valid_cp = np.arange(1,len(parent1_chrom))
    # Sample two crossing points from valid_cp without repetition
    samples = np.random.choice(valid_cp, 2, replace=False)
    cross_pt1 = samples[0]
    cross_pt2 = samples[1]
    # Make sure that cross_pt1 < cross_pt2
    if cross_pt1 > cross_pt2:
        temp = cross_pt1
        cross_pt1 = cross_pt2
        cross_pt2 = temp
    # First child
    part1 = parent1_chrom[0:cross_pt1]
    part2 = parent2_chrom[cross_pt1:cross_pt2]
    part3 = parent1_chrom[cross_pt2:]
    child1 = np.concatenate((part1, part2, part3))
    # Second child
    part1 = parent2_chrom[0:cross_pt1]
    part2 = parent1_chrom[cross_pt1:cross_pt2]
    part3 = parent2_chrom[cross_pt2:]
    child2 = np.concatenate((part1, part2, part3))
    # Decide if recombined children make it to the next generation
    R1 = np.random.uniform()
    if R1 > pc:
        child1 = parent1_chrom  # do not recombinate
    R2 = np.random.uniform()
    if R2 > pc:
        child2 = parent2_chrom  # do not recombinate
    # Return the offspring
    return child1, child2
