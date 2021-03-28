# -----------------------------------------------------------
#                   Selection by Tournament
# -----------------------------------------------------------
# Inputs:
#   pop_chrom   - population of individuals
#   pop_fit     - fitness value of each individual
# Outputs:
#   p1_chrom    - chromosome of the first parent
#   p2_chrom    - chromosome of the second parent
# -----------------------------------------------------------
# file: selection_tournament.py
# -----------------------------------------------------------
import numpy as np
import random
# -----------------------------------------------------------
def selection_tournament(pop_chrom, pop_fit):
    # number of individuals in the population
    M = np.shape(pop_chrom)[0]
    if M <= 3:
        print('selection_tournament --> M must be bigger than 3')
        exit()
    # randomly select num_indvs individuals without replacement
    num_indvs = 3 # this number could be a formal parameter
    inds = random.sample(range(1, M), num_indvs)
    selected_indvs = pop_chrom[inds]
    selected_fits = pop_fit[inds]
    # sort in descending order
    sorted_idx = np.argsort(-selected_fits)
    # pick the two most fit individuals
    ind_p1 = sorted_idx[0]
    p1_chrom = selected_indvs[ind_p1]
    ind_p2 = sorted_idx[1]
    p2_chrom = selected_indvs[ind_p2]
    # return selected parents
    return p1_chrom, p2_chrom

