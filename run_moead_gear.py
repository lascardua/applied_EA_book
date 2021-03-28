# ------------------------------------------------------------
#          MOEA/D Optimization for the Gear Train System
# ------------------------------------------------------------
# file: run_moead_gear.py
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from case_study_gear.f_goal_gear import f_Gear
from moead_rep.algs.moead_int import moead_int
from case_study_gear.gear_true_PF import true_PF
# ------------------------------------------------------------

# Define the optimization problem
f_goal = f_Gear                     # goal function
n_dim = 4                           # 4 decision variables
n_goals = 2                         # number of individual goals
ubc = 60                            # upper and lower bounds
lbc = 12
lb = lbc*np.ones(n_dim,dtype=int)
ub = ubc*np.ones(n_dim,dtype=int)

pc = 1.0                            # crossover probability
pm = 0.6                            # mutation probability


# Optimization process
M  = 4000                   # number of optimization iterations
Ne = 500                    # maximum number of individuals in
                            # the external population
# Set MOEAD hyperparameters
N    = 50
T = np.maximum(np.ceil(0.15 * N), 2)   # number of neighbors
T = np.minimum(np.maximum(T,2),15)
T = np.int(T)

v = np.arange(lbc,ubc+1)            # list of valid gene values

# Call the optimization algorithm
F_cost, F_chrom = moead_int(N, Ne, M, T, f_goal, lb, ub,
                            n_goals, pc, pm, v)
# Save the optimization results
f_fit_file = 'moead_f_cost.npy'
f_chrom_file = 'moead_f_chrom.npy'
np.save(f_fit_file, F_cost)
np.save(f_chrom_file, F_chrom)


# Plot the scores per iteration
str = "Gear Train System"
plt.scatter(F_cost[:,0], F_cost[:,1], label='MOEA/D', marker='.', c='k'),
plt.scatter(true_PF[:,0], true_PF[:,1], label='true PF', marker='+', c='k')
plt.title(str)
plt.ylabel('$f_{1}$')
plt.xlabel('$f_{0}$')
plt.legend()
plt.show()





        


