# --------------------------------------------------
#      Solving G08 with a Continuous GA
# --------------------------------------------------
# file: solve_g08_gac.py
# --------------------------------------------------
import numpy as np
# function that creates a random population
from auxiliary.init_rv import init_rv
# fitness function for minimizing G08
from fitnessf_max.fitnessf_g08 import fitness_g08
# function that implements linear ranking selection
from operators_rep.selection.selection_linear_ranking_sus \
    import selection_linear_ranking_sus
# function that implements uniform crossover
from operators_rep.crossover.crossover_rv_blending \
    import blending_crossover
# function that implements gaussian mutation
from operators_rep.mutation.mutation_gaussian_rv \
    import mutation_gaussian_rv
# function that implements the continuous GA
from ga_rep.algs.gac import gac
# --------------------------------------------------
# 1 - Define the upper and lower bounds of the search space
ndim = 2                # Number of dimensions of the problem
ubc = 5
lbc = -5
lb = lbc*np.ones(ndim)# lower bound for the search space
ub = ubc*np.ones(ndim)# upper bound for the search space
# --------------------------------------------------
# 2 - Define parameters for the optimization
npop = 100            # number of individuals in the population
maxIterations = 200  # maximum number of iterations
# --------------------------------------------------
# 3 - Parameters for the GA
pc = 0.8        # crossover probability
pm = 0.1        # mutation probability
er = 0.1        # elitism rate

initf       = init_rv                   # creates the initial population
fitnessf    = fitness_g08               # fitness function
crossoverf  = blending_crossover        # implements crossover
mutationf   = mutation_gaussian_rv      # implements mutation
selectionf  = \
    selection_linear_ranking_sus        # implements selection
# --------------------------------------------------
# 4 - Call the genetic algorithm
best_chrom, _ = gac(npop,
                    maxIterations,\
                    pc,pm,er,\
                    fitnessf, \
                    selectionf,
                    crossoverf,\
                    mutationf,lb,ub)
# --------------------------------------------------
# 5 - Print the results found
from test_functions_rep.so.g08 import g08
best_fval,_,_ = g08(best_chrom)
print('The minimum value of G08 is %.5f'%(best_fval))
print('The minimum is located at ',best_chrom)
# --------------------------------------------------




