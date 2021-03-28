# ------------------------------------------------------------
#                     so_perform_MC_runs
#  Monte Carlo runs of a minimization process using a GA
# ------------------------------------------------------------
# file: so_monte_carlo_runs.py
# ------------------------------------------------------------
# fitness_f - function to be maximized
# n_dim     - dimensionality of the search space
# lb        - lower bound of the search space
# ub        - upper bound bound of the search space
# nMC       - number of simulations to be performed
# ------------------------------------------------------------
import numpy as np
from auxiliary.init_rv import init_rv
from operators_rep.selection.selection_linear_ranking_sus \
    import selection_linear_ranking_sus
from operators_rep.crossover.crossover_uniform \
    import crossover_uniform
from operators_rep.mutation.mutation_uniform_rv \
    import mutation_uniform_rv
from operators_rep.elitism.elitism import elitism
from ga_rep.algs.gac import gac
# ------------------------------------------------------------
def perform_MC_runs(fitness_f, n_dim, lb, ub, nMC):
    # 1 - Define the parameters of the optimization
    npop = 20            # Number of individuals in the population
    maxIterations = 300  # Maximum number of iterations

    # 2 - Parameters for the algorithm
    pc          = 0.9        # Crossover probability
    pm          = 0.5        # Mutation probability
    er          = 0.1        # Elitism rate
    init_f      = init_rv              # Creates the initial population
    crossover_f = crossover_uniform    # Implements crossover
    mutation_f  = mutation_uniform_rv  # Implements mutation
    elitism_f   = elitism              # Implements elitism
    selection_f = \
        selection_linear_ranking_sus    # Implements selection

    # 3 - Run the GAc algorithm
    best_thetas  = np.zeros((nMC, n_dim)) # Store the best solutions
    np.random.seed(123)                 # For repeatability
    for id_MC in range(nMC):            # Monte Carlo runs
        a, _ = gac(npop, maxIterations, pc, pm,
                      er, fitness_f, selection_f, crossover_f,
                      mutation_f,  lb, ub)
        best_thetas[id_MC] = a
    # Return the solutions found
    return best_thetas