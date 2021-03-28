# --------------------------------------------------
#      GAb Algorithm Minimizing a Sphere
# --------------------------------------------------
# file: fig_gab_sphere.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from encoding_rep.gray2dec import gray2decInterval
from fitnessf_max.fitnessf_sphere_gray import \
    fitness_sphere_gray
from encoding_rep.gen2phen import gen2phen
from operators_rep.selection.selection_tournament import \
    selection_tournament
from operators_rep.crossover.crossover_dp import \
    crossover_dp
from operators_rep.mutation.mutation_binary import \
    mutation_binary
from ga_rep.algs.gab import gab
# --------------------------------------------------
# 1 - Define the search space
ndim = 20               # Number of dimensions of the problem
lb = -5*np.ones(ndim)   # lower bound for the search space
ub = 5*np.ones(ndim)    # upper bound for the search space
nbits_var = 4           # number of bits to represent a single
                        # decision variable
nbits_word = ndim*nbits_var # number of genes used to represent
                        # the vector of decision variables

# 2 - Define the parameters for the optimization
npop = 30            # number of individuals in the population
maxIterations = 300  # maximum number of iterations


# 3 - Parameters for the algorithm
pc = 0.8        # crossover probability
pm = 0.1        # mutation probability
er = 0.1        # elitism rate
crossoverf  = crossover_dp         # implements crossover
mutationf   = mutation_binary      # implements mutation
selectionf  = \
    selection_tournament           # implements selection
fitnessf = fitness_sphere_gray     # fitness function

# 4 - Run the binary GA
best_theta, best_scores = gab(npop, maxIterations, pc, pm,
                            er, fitnessf, selectionf, crossoverf,
                            mutationf, lb, ub,nbits_word)

# 5 - Convert binary coded "best_theta" into a real-value
# number in [lb, ub]
best_theta = gen2phen(gray2decInterval,best_theta,ndim,lb,ub,nbits_word)
# remove an unused dimension in best_scores
best_scores = np.squeeze(best_scores)

# 6 - Plot the convergence curves
from auxiliary.plot_convergence_curve \
    import plot_convergence_curve
fig_file = 'figure_6_2.eps'
title_str = \
    "Binary GA Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,-best_scores)


