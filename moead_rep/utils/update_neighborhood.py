# -----------------------------------------------------
# Update of neighboring solutions
# -----------------------------------------------------
# id_p          - index of the solution whose neighbors are
#               being updadted
# B             - matrix where each ith row is the vector
#               of indexes of the ith solution
# pop_chrom - individuals of the population
# pop_cost  - costs of the individuals of the population
# y_chrom   - new child
# y_cost    - cost of the new child
# z         - reference point
# lambd     - weight vectors
# -----------------------------------------------------
# file: update_neighborhood.py
# -----------------------------------------------------
from moead_rep.utils.scalarized_cost import scalarized_cost
# -----------------------------------------------------
def update_solutions_in_B(id_p, B, pop_chrom, pop_cost,
                          y_chrom, y_cost, z, lambd):
    # Get the ids of the subproblems in the vicinity of
    # subproblem id_p
    ids_n = B[id_p]
    # For each subproblem id_n in the neighborhood
    for id_n in ids_n:
        # Compute the scalarized cost of the new
        # candidate solution
        y_prime_g = scalarized_cost(y_cost,
                                    z, lambd[id_n])
        # Compute the scalarized cost of the
        # current candidate solution
        pop_g = scalarized_cost(pop_cost[id_n],
                                z, lambd[id_n])
        # If the new candidate solution produces a
        # smaller scalarized cost than the current
        # candidate solution, replace the current
        # candidate solution with the new candidate
        # solution
        if y_prime_g < pop_g:
            pop_chrom[id_n] = y_chrom
            pop_cost[id_n] = y_cost
    return pop_chrom, pop_cost