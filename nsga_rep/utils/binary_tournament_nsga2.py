# -----------------------------------------------------------
#          Binary Tournament for NSGA-II
# -----------------------------------------------------------
# Inputs:
#   pop_chrom     - population of candidate solutions
#   pop_rank      - rank of each individual in pop_chrom
#   pop_cdist     - crowding distance of each individual in
#                     pop-chrom
# Outputs:
# parent1         - first selected parent
# parent2         - second selected parent
# -----------------------------------------------------------
# file: binary_tournament_nsga2.py
# -----------------------------------------------------------
import random
import numpy as np
from nsga_rep.utils.crowded_comparison import \
    crowded_comparison_operator
# -----------------------------------------------------------
def binary_tournament(pop_chrom, pop_rank, pop_cdist):
    # number of chromosomes
    M = np.shape(pop_chrom)[0]
    # randomly select num_indvs individuals without replacement
    num_indvs = 3 # this number could be a formal parameter
    inds = random.sample(range(1, M), num_indvs)
    # selected individuals
    selected_chroms = pop_chrom[inds]
    selected_ranks = pop_rank[inds]
    selected_cdists = pop_cdist[inds]

    # select two parents using the crowded comparison operator
    # nc - counts victories in the comparison
    nc = np.zeros(num_indvs, dtype=int)
    for i in range(num_indvs):
        p0_rank = selected_ranks[i]
        p0_cdist = selected_cdists[i]
        for j in range(i+1,num_indvs):
            p1_rank  = selected_ranks[j]
            p1_cdist =  selected_cdists[j]
            # calculate the cco
            cco = crowded_comparison_operator(p0_rank, p0_cdist,
                                              p1_rank, p1_cdist)
            # counts the victory in the comparison
            if cco == 0:
                nc[i] = nc[i] + 1
            else:
                nc[j] = nc[j] + 1

    # sort in descending order of victories
    inds_nc = np.argsort(-nc)
    # return the first two in number of victories
    ind_p1 = inds_nc[0]
    parent1 = selected_chroms[ind_p1]
    ind_p2 = inds_nc[1]
    parent2 = selected_chroms[ind_p2]

    return parent1, parent2



