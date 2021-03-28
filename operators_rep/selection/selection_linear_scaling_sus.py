
from operators_rep.selection.fitness_linear_scaling import fitness_linear_scaling
from operators_rep.selection.sampling_sus import sampling_sus
# This function can be used by both discrete and continuous GAs
def selection_linear_scaling_sus(pop_chrom, pop_fit):
    # Fitness scaling
    pop_fit = fitness_linear_scaling(pop_fit)
    # Sampling
    pop_chrom, pop_fit = sampling_sus(pop_chrom, pop_fit)
    return pop_chrom, pop_fit