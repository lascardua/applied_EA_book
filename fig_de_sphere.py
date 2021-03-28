# --------------------------------------------------
#      DE Algorithm Minimizing a Sphere
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from de_rep.algs.de import de
from test_functions_rep.so.sphere import sphere
# Repeatability
np.random.seed(123)

# 1 - Define the upper and lower bounds of the search space
n_dim = 20               # Number of dimensions of the problem
ubc = 5
lbc = -5
lb = lbc*np.ones(n_dim)  # lower bound for the search space
ub = ubc*np.ones(n_dim)  # upper bound for the search space

# 2 - Define the parameters for the optimization
max_iters = 300  # maximum number of iterations
nMC = 10         # number of MC runs

# 3 - Parameters for the algorithm
pc = 0.9 # crossover probability
theta_0 = np.random.rand(n_dim, nMC)  # random initial solution
pop_size = 20   # number of individuals in the population

# 4 - Define the cost function
f_cost = sphere

# 5 - Run the DE algorithm
best_theta  = np.zeros((n_dim, nMC))
best_scores = np.zeros((max_iters,nMC))
np.random.seed(123) # for repeatability
for id_run in range(nMC):
    # call DE
    [a, b] = de(f_cost,pop_size, max_iters,
                pc, lb, ub, step_size = 0.8)
    # store the best solution found
    best_theta[:, id_run] = a
    # Store the vector on minimum values found in
    # each iteration of the algorithm
    # Squeeze - remove an unsed dimension in b
    best_scores[:, id_run] = np.squeeze(b)

# 6 - Plot the convergence curves--------------------------
# Not necessary for solving the problem
from auxiliary.plot_convergence_curve import plot_convergence_curve
fig_file = 'figure_7_2.eps'
title_str = "DE Minimizing a " + str(n_dim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,best_scores)


