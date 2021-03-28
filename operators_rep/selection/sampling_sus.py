# -----------------------------------------------------------
#             Stochastic Universal Sampling
# -----------------------------------------------------------
# Selects two parents using stochastic universal sampling
# -----------------------------------------------------------
# Inputs:
#   pop_chrom   - individuals of the population
#   pop_fit     - corresponding fitness values
# Outputs:
#   parent1     - chromosome of the first parent
#   parent2     - chromosome of the second parent
# -----------------------------------------------------------
#  file: sampling_sus.py
# -----------------------------------------------------------
import numpy as np
# -----------------------------------------------------------
def sampling_sus(pop_chrom, pop_fit):
    # number of individuals
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
    N = 2 # number of offspring to keep
    F = sum(temp_pop_fit) # total fitness of the population
    P = F / N # distance between the pointers (F/N)
    # sample from uniform distribution a starting point for
    # the pointers
    start = P*np.random.uniform(0,1) # in [0,P]
    ptr = np.zeros(N)
    # compute ending points for both pointers
    for id in range(N):
        ptr[id]= start + id * P
    # select first parent id
    parent1_idx = sorted_idx[0]
    for i in range(M):
        if (ptr[0] < cumsum[i]):
            parent1_idx = i
            break
    # select second parent id
    parent2_idx = sorted_idx[0]
    for i in range(M):
        if (ptr[1] < cumsum[i]):
            parent2_idx = i
            break
    # pick the chromosomes corresponding to
    # the parents' ids
    parent1 = temp_pop_chrom[parent1_idx]
    parent2 = temp_pop_chrom[parent2_idx]
    # return the selected parents
    return parent1, parent2
