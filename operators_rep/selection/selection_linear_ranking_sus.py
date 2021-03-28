# -----------------------------------------------------------
# Selection by Linear Ranking and Stochastic Universal Sampling
# -----------------------------------------------------------
# pop_chrom     - population
# pop_fit       - fitness values of the population
# -----------------------------------------------------------
# file: selection_linear_ranking_sus.py
# -----------------------------------------------------------
from operators_rep.selection.fitness_linear_ranking import fitness_linear_ranking
from operators_rep.selection.sampling_sus import sampling_sus
# -----------------------------------------------------------
def selection_linear_ranking_sus(pop_chrom, pop_fit):
    # Fitness linear ranking
    pop_chrom, pop_fit = fitness_linear_ranking(pop_chrom, pop_fit)
    # Stochastic universal sampling
    p1_chrom, p2_chrom = sampling_sus(pop_chrom, pop_fit)
    return p1_chrom, p2_chrom