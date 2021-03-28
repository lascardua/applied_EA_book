# -----------------------------------------------------------
#                 Fitness Linear Scaling
# Computes the normalized fitness values of the population
# using linear fitness scaling
# -----------------------------------------------------------
# Inputs:
#   pop_fit      - fitness values of the population members
# Outputs
#   norm_fitness - normalized fitness values
# Usage:
#   fits = np.array([2,8,20,18,6])
#   norm_fits = fitness_linear_scaling(fits)
# -----------------------------------------------------------
# file: fitness_linear_scaling.py
# -----------------------------------------------------------
import numpy as np
# -----------------------------------------------------------
def fitness_linear_scaling(pop_fit):
    M = np.shape(pop_fit)[0]
    # Linear scaling
    # scaled(f) = a * f + b
    a = 1
    b = abs( min(  pop_fit  ))
    scaled_fitness = a * pop_fit + b
    # Computes normalized fitness values
    norm_fitness = scaled_fitness / np.sum(scaled_fitness)
    # Returns normalized fitness values
    return norm_fitness


