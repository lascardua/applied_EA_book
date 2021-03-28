
from operators_rep.selection.fitness_linear_ranking import fitness_linear_ranking
from operators_rep.selection.sampling_rw import sampling_rw
# This function can be used by both discrete and continuous GAs
def selection_linear_ranking_rw(pop_chrom, pop_fit):
    # Fitness scaling
    pop_chrom, pop_fit = fitness_linear_ranking(pop_chrom, pop_fit)
    # Sampling
    pop_chrom, pop_fit = sampling_rw(pop_chrom, pop_fit)
    return pop_chrom, pop_fit