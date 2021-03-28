# -----------------------------------------------------------
#                 Fitness Exponential Ranking
# -----------------------------------------------------------
#   pop_chrom   - individuals in the population
#   pop_fit     - fitness values of the individuals
# Outputs:
#   newpop_chrom- individuals sorted in descending ranking order
#   newpop_fit  - ranks of the individuals
# Usage:
#   pop_chrom = np.array([1, 2, 3, 4])
#   pop_fit = np.array([10, 5, 70, 15])
#   np_ch, np_f = fitness_exponential_ranking(pop_chrom, pop_fit)
# -----------------------------------------------------------
# file: fitness_exponential_ranking.py
# -----------------------------------------------------------
import numpy as np
# -----------------------------------------------------------
def fitness_exponential_ranking(pop_chrom, pop_fit):
    # number of individuals in the population
    N = np.shape(pop_chrom)[0]
    # fitness of the best individual
    s = 0.99
    # sort in descending fitness order
    sorted_idx = np.argsort(-pop_fit)
    # sorted population
    newpop_chrom = np.zeros_like(pop_chrom)
    # rank values
    newpop_fit = np.zeros_like(pop_fit, dtype=float)
    # compute the ranks
    for i in range(1,N+1):
        newpop_chrom[i-1] = pop_chrom[sorted_idx[i-1]]
        newpop_fit[i-1] = s**(i-1)
    # return the sorted population and the corresponding
    # ranks
    return newpop_chrom, newpop_fit