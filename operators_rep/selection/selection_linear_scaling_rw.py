# -----------------------------------------------------------
#       Selection Linear Scaling Roulette Wheel
# -----------------------------------------------------------
# Selection with fitness linear scaling with roulette wheel
# sampling
# -----------------------------------------------------------
# Inputs:
#   pop_chrom   - population of individuals
#   pop_fit     - fitness value of each individual
# Outputs:
#   p1_chrom    - chromosome of the first parent
#   p2_chrom    - chromosome of the second parent
# -----------------------------------------------------------
# file: selection_linear_scaling_rw.py
# -----------------------------------------------------------
from operators_rep.selection.sampling_rw import sampling_rw
from operators_rep.selection.fitness_linear_scaling import \
    fitness_linear_scaling
# -----------------------------------------------------------
def selection_linear_scaling_rw(pop_chrom, pop_fit):
    # Fitness scaling
    pop_fit = fitness_linear_scaling(pop_fit)
    # Sampling
    p1_chrom, p2_chrom = sampling_rw(pop_chrom, pop_fit)
    return p1_chrom, p2_chrom