# -----------------------------------------------------------
# Selection by Exponential Ranking and Stochastic Universal
#                       Sampling
# -----------------------------------------------------------
# Inputs:
#   pop_chrom   - population of individuals
#   pop_fit     - fitness value of each individual
# Outputs:
#   p1_chrom    - chromosome of the first parent
#   p2_chrom    - chromosome of the second parent
# -----------------------------------------------------------
# file: selection_exponential_ranking_sus.py
# -----------------------------------------------------------
from operators_rep.selection.fitness_exponential_ranking import \
    fitness_exponential_ranking
from operators_rep.selection.sampling_sus import sampling_sus
# -----------------------------------------------------------
def selection_exponential_ranking_sus(pop_chrom, pop_fit):
    # Fitness scaling
    pop_chrom, pop_fit = fitness_exponential_ranking(pop_chrom, pop_fit)
    # Sampling
    p1_chrom, p2_chrom = sampling_sus(pop_chrom, pop_fit)
    return p1_chrom, p2_chrom