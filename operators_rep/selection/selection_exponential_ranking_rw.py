
from operators_rep.selection.fitness_exponential_ranking import fitness_exponential_ranking
from operators_rep.selection.sampling_rw import sampling_rw
# This function can be used by both discrete and continuous GAs
def selection_exponential_ranking_rw(pop_chrom, pop_fit):
    # Fitness scaling
    pop_chrom, pop_fit = fitness_exponential_ranking(pop_chrom, pop_fit)
    # Sampling
    pop_chrom, pop_fit = sampling_rw(pop_chrom, pop_fit)
    return pop_chrom, pop_fit