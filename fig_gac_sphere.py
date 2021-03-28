# --------------------------------------------------
#      GAc Algorithm Minimizing a Sphere
# --------------------------------------------------
# file: fig_gac_sphere.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from fitnessf_max.fitnessf_sphere_rv import \
    fitness_sphere_rv
from operators_rep.selection.selection_tournament import \
    selection_tournament
from operators_rep.crossover.crossover_rv_sbx import \
    sbx_crossover
from operators_rep.mutation.mutation_polynomial_rv import \
    mutation_polynomial_rv
from ga_rep.algs.gac import gac
# --------------------------------------------------
# 1 - Define the upper and lower bounds of the search space
ndim = 20               # Number of dimensions of the problem
lb = 5*np.ones(ndim)  # lower bound for the search space
ub = -5*np.ones(ndim)  # upper bound for the search space

# 2 - Define the parameters for the optimization
npop = 30            # number of individuals in the population
maxIterations = 300  # maximum number of iterations

# 3 - Parameters for the algorithm
pc = 0.5        # crossover probability
pm = 0.8        # mutation probability
er = 0.1        # elitism rate
crossoverf  = sbx_crossover             # implements crossover
mutationf   = mutation_polynomial_rv    # implements mutation
selectionf  = selection_tournament      # implements selection
ffitness    = fitness_sphere_rv         # fitness function

# 4 - Run the GA algorithm
best_theta, best_scores = gac(npop, maxIterations, pc, pm,
                    er, ffitness,
                    selectionf, crossoverf,
                    mutationf, lb, ub)
# remove an unsed dimension in best_scores
best_scores= np.squeeze(best_scores)

# 5 - Plot the convergence curve
# Not necessary for solving the problem
from auxiliary.plot_convergence_curve \
    import plot_convergence_curve
fig_file = 'figure_6_1.eps'
title_str = \
    "Continuous GA Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,-best_scores)


