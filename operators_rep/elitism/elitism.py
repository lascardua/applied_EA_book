# -----------------------------------------------------------
#                   Elitism
# Implements elitism by replacing the worst M of the N
# children received  with the M elite individuals of the
# last generation (pop_chrom)
# -----------------------------------------------------------
# Inputs:
#   pop_chrom       - individuals of the last generation
#   pop_fit         - fitness values of the individuals
#   children_chrom  - new individuals
#   children_fit    - fitness values of the new individuals
# Outputs:
#   new_pop_chrom   - new population
#   new_pop_fit     - fitness of the new population
# -----------------------------------------------------------
# file: elitism.py
# -----------------------------------------------------------
import numpy as np
def elitism(pop_chrom, pop_fit, children_chrom, children_fit, er):
    # Compute number of individuals in the population
    N = np.shape(pop_chrom)[0]
    # Compute number of elite chromosomes
    M = int(np.ceil(N * er))
    # Sort the N children in descending fitness order
    ids_sorted = np.argsort(-children_fit)
    # Keep only the best N - M children
    ids_sorted = ids_sorted[0:(N - M)]
    children_chrom = children_chrom[ids_sorted]
    children_fit = children_fit[ids_sorted]
    # Pick the best M individuals of the current population
    ids_sorted = np.argsort(-pop_fit)
    ids_sorted = ids_sorted[0:M]
    best_pop_chrom = pop_chrom[ids_sorted]
    best_pop_fit = pop_fit[ids_sorted]
    # Replace the worst M children with the M elite chromosomes of the
    # last generation
    new_pop_chrom = np.vstack((children_chrom, best_pop_chrom))
    new_pop_fit = np.hstack((children_fit,best_pop_fit))
    # Return the new population and the corresponding fitness values
    return new_pop_chrom, new_pop_fit


