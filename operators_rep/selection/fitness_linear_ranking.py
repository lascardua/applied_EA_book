# -----------------------------------------------------------
#                 Fitness Linear Ranking
#     Computes the ranks of the individuals in the population
# -----------------------------------------------------------
# Inputs:
#   pop_chrom   - individuals in the population
#   pop_fit     - fitness values of the individuals
# Outputs:
#   newpop_chrom- individuals sorted in descending ranking order
#   newpop_fit  - ranks of the individuals
# Usage:
#   pop_chrom = np.array([1, 2, 3, 4])
#   pop_fit = np.array([10, 5, 70, 15])
#   npop_ch, npop_f = fitness_linear_ranking(pop_chrom, pop_fit)
# -----------------------------------------------------------
# file: fitness_linear_ranking.py
# -----------------------------------------------------------
import numpy as np
# -----------------------------------------------------------
def fitness_linear_ranking(pop_chrom, pop_fit):
    # NUmber of individuals in the population
    M = np.shape(pop_fit)[0]
    # Fitness of the best individual
    # Attention to the valid interval --> 1< s <= 2"
    s = 1.5
    # sort in descending fitness order
    sorted_idx = np.argsort(-pop_fit)
    # Sorted population according to ranks
    newpop_chrom = np.zeros_like(pop_chrom)
    # Ranks of the sorted individuals
    newpop_fit = np.zeros_like(pop_fit, dtype = float)
    # Fitness for intermediate individuals
    for i in range(1,M+1):
        newpop_chrom[i-1] = pop_chrom[sorted_idx[i-1]]
        newpop_fit[i-1] = s - (2 * (i - 1) * (s - 1)) / (M - 1)
    # Return the sorted individuals and their ranks
    return newpop_chrom, newpop_fit