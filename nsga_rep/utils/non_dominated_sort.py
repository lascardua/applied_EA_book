# -----------------------------------------------------------
#            Fast Non-Dominated Sorting
# -----------------------------------------------------------
# Inputs:
#   pop_chrom     - population of candidate solutions
#   pop_cost      - cost of each individual in pop_chrom
# Outputs:
#   F             - Pareto fronts
#   pop_rank      - rank of each solution
# -----------------------------------------------------------
# file: non_dominated_sort.py
# -----------------------------------------------------------
import numpy as np
# -----------------------------------------------------------
def fast_non_dominated_sort(pop_chrom, pop_cost):
    n_pop = len(pop_cost)
    # Rank of each candidate solution
    pop_rank = np.zeros(n_pop, dtype=int)
    # Set of solutions that solution p dominates
    S = [[] for _ in range(n_pop)]
    # Number of solutions that dominate solution p
    n = np.zeros(n_pop, dtype=int)
    # Pareto fronts
    F = [[]]
    # For each candidate solution p_idx
    for p_idx in range(n_pop):
        # for each candidate solution q_idx
        for q_idx in range(n_pop):
            if p_idx == q_idx:
                continue
            # if solution p_idx dominates solution q_idx
            if dominates(pop_cost[p_idx], pop_cost[q_idx]):
                # add solution q_idx to S_{p_idx}
                S[p_idx].append(q_idx)
            elif dominates(pop_cost[q_idx], pop_cost[p_idx]):
                # increase the number of solutions that dominate
                # solution p_idx
                n[p_idx] = n[p_idx] + 1
        # If no solution dominates solution p_idx
        if n[p_idx] == 0:
            # add solution p_idx to the first Pareto front
            pop_rank[p_idx] = 0
            F[0].append(p_idx)
    # Build the other Pareto fronts
    i = 0  # initialize the front counter
    while (F[i] != []):
        # used to store the members of the next front
        Q = []
        # for each solution p_idx in the ith front
        for p_idx in F[i]:
            # for each solution q_idx dominated by
            # solution p_idx
            for q_idx in S[p_idx]:
                # decrease the number of solutions that
                # dominate solution q_idx
                n[q_idx] = n[q_idx] - 1
                # if the number of solutions that dominate
                # solution q_idx has reached zero
                if (n[q_idx] == 0):
                    # then all solutions that dominate
                    # solution q_idx are from fronts
                    # numbered i or bellow, this means
                    # that solution q_idx belongs to
                    # front i + 1
                    pop_rank[q_idx] = i + 1
                    if q_idx not in Q:
                        Q.append(q_idx)
        i = i + 1
        F.append(Q)
    del F[len(F) - 1]

    return F, pop_rank
# -----------------------------------------------------------
# Returns 1 if x dominates y, otherwise returns 0
# -----------------------------------------------------------
def dominates(x, y):
    if all(x <= y) and any(x < y):
        return 1
    else:
        return 0
