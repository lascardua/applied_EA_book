# ------------------------------------------------------------
#                   DOMINATES
# ------------------------------------------------------------
# cost_x   - k-dimensional cost of candidate solution X
# cost_y   - k-dimensional cost of candidate solution Y
# ------------------------------------------------------------
import numpy as np
def dominates(cost_x,cost_y):
    if all(cost_x <= cost_y) and any(cost_x < cost_y):
        return 1
    else:
        return 0

# ------------------------------------------------------------
#          FIND NON-DOMINATED SOLUTIONS
# ------------------------------------------------------------
# pop_chrom   - matrix of N n-dimensional candidate solutions
# pop_cost    - matrix of N k-dimensional costs of the candidate
#               solutions
# ------------------------------------------------------------
def find_non_dominated(pop_chrom, pop_cost):
    M = len(pop_cost)
    # If the ith position of
    # "dominated" is 1, then the ith candidate
    # solution in pop_chrom is dominated
    dominated = np.zeros(M)
    # for each solution in pop_chrom
    for idx in range(M):
        # Check if pop_chrom[idx]
        # dominates pop_chrom[idy]
        for idy in range(M):
            if idx == idy:
                continue
            # if pop_chrom[idx] dominates
            # pop_chrom[idy]
            if dominates(pop_cost[idx], pop_cost[idy]):
                # mark pop_chrom[idy] as dominated
                dominated[idy] = 1
    # find the indexes of all non-dominated solutions
    ids_non_dominated = np.where(dominated == 0)
    # non-dominated solutions and their costs
    non_dominated_pop = pop_chrom[ids_non_dominated]
    non_dominated_cost = pop_cost[ids_non_dominated]
    # return non-dominated solutions and their costs
    return non_dominated_pop, non_dominated_cost