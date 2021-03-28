# -----------------------------------------------------------
#                 Roulette-Wheel Sampling
# -----------------------------------------------------------
# This function can be used with both discrete and real-valued
# representations
# -----------------------------------------------------------
# file: sampling_rw.py
# -----------------------------------------------------------
import numpy as np
def sampling_rw(pop_chrom, pop_fit):
    # number of chromosomes
    M = np.shape(pop_chrom)[0]
    # sort in ascending order
    sorted_idx = np.argsort(pop_fit)
    # temporary population
    temp_pop_chrom = pop_chrom[sorted_idx]
    temp_pop_fit   = pop_fit[sorted_idx]
    # cumulative sum of ordered fitness values
    cumsum = np.zeros(M)
    cumsum[0] = temp_pop_fit[0]
    for i in range(1,M):
        for j in range(i+1):
            cumsum[i] = cumsum[i] + temp_pop_fit[j]
    # sample from uniform distribution
    R = np.random.uniform(0,1) # in [0,1]
    # select first parent
    parent1_idx = 0
    for i in range(M):
        if R < cumsum[i]:
            parent1_idx = i
            break
    # select second parent
    parent2_idx = parent1_idx
    while parent2_idx == parent1_idx:
        R = np.random.uniform(0,1) # in [0,1]
        for i in range(M):
            if R < cumsum[i]:
                parent1_idx = i
                break
    parent1 = temp_pop_chrom[parent1_idx]
    parent2 = temp_pop_chrom[parent2_idx]
    return parent1, parent2

