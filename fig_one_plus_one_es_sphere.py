# --------------------------------------------------
#      1 + 1 ES Algorithms Minimizing a Sphere
# --------------------------------------------------
# file: fig_one_plus_one_es_sphere.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from es_rep.algs.one_plus_one_es import one_plus_one_es
from es_rep.algs.one_plus_one_1_5th_es import one_plus_one_es_1_5th
from test_functions_rep.so.sphere import sphere
# --------------------------------------------------
# 0 - For repeatability
np.random.seed(123)

# 1 - Define the upper and lower bounds of the search space
ndim = 20               # Number of dimensions of the problem
lb = -5*np.ones(ndim)   # Bounds of the search space
ub = 5*np.ones(ndim)

# 2 - Define the parameters for the optimization
maxIterations = 300  # maximum number of iterations
nMC = 10             # number of MC runs

# 3 - Parameters for the algorithm
theta_0 = np.random.rand(ndim,nMC)  # random initial solution

# 4 - Define the cost function
loss = sphere

# 5 - Run the (1+1) ES algorithm
best_theta  = np.zeros((ndim,nMC))
best_scores = np.zeros((maxIterations,nMC))
for id_run in range(nMC):
    np.random.seed(123)
    [a, b] = one_plus_one_es(loss, theta_0[:,id_run], maxIterations, lb, ub)
    best_theta[:, id_run] = a
    best_scores[:, id_run] = np.squeeze(b) # remove an unsed dimension in b


# 6 - Plot the convergence curve
from auxiliary.plot_convergence_curve import plot_convergence_curve
fig_file = 'figure_5_4.eps'
title_str = \
    "(1+1)-ES Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,best_scores)

# 7 - Run the (1+1) 1/5th rule ES algorithm
best_theta  = np.zeros((ndim,nMC))
best_scores = np.zeros((maxIterations,nMC))
for id_run in range(nMC):
    np.random.seed(123)
    [a, b] = one_plus_one_es_1_5th(loss, theta_0[:,id_run], maxIterations, lb, ub)
    best_theta[:, id_run] = a
    # remove an unused dimension in b
    best_scores[:, id_run] = np.squeeze(b)


# 8 - Plot the convergence curve
from auxiliary.plot_convergence_curve import plot_convergence_curve
fig_file = 'figure_5_5.eps'
title_str = \
    "(1+1)-ES with 1/5th Rule Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,best_scores)
