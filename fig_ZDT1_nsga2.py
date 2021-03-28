# --------------------------------------------------
# Multi-Objective Optimization Using NSGA-II Algorithm
#            to Minimize the ZDT1 Function
# --------------------------------------------------
# file: fig_ZDT1_nsga2.py
# --------------------------------------------------
import numpy as np
from auxiliary.init_rv import init_rv
from nsga_rep.algs.nsga2 import nsga2
from test_functions_rep.mo.zdt1 import zdt1
from operators_rep.crossover.crossover_rv_sbx import sbx_crossover
from operators_rep.mutation.mutation_gaussian_rv import mutation_gaussian_rv

# -- Problem Setting
fname = "ZDT1"
n_dim = 30

# -- Configuring the optimization
max_iterations = 300 # number of optimization iterations
pop_size = 100      # number of individuals in the population

# -- Configure NSGA-II
pc = 0.9            # crossover probability
pm = 0.1            # mutation probability

f_init  = init_rv                # initiates a random population
f_cross = sbx_crossover          # performs crossover
f_mut   = mutation_gaussian_rv  # performs mutation

# --- Optimization
# the ZDT1 problem
f_cost = zdt1
n_goals = 2
lb = 0*np.ones(n_dim)
ub = 1*np.ones(n_dim)
# perform the optimization
F_cost, F_chrom = nsga2(pop_size, max_iterations, pc,
                                  pm, f_init, f_cost, f_cross,
                                  f_mut, lb, ub, n_dim, n_goals)


# --- PLOT
# plot the approximate Pareto front
import matplotlib.pyplot as plt
plt.xlabel('$f_1$', fontsize=15)
plt.ylabel('$f_2$', fontsize=15)
plt.scatter(F_cost[:, 0], F_cost[:, 1], marker=".", color='k', label='NSGA2')
ll = fname + ' - ' + str(n_dim) + ' dimensions'
plt.title(ll)
plt.legend()
plt.xlim(0,1)
plt.show()





