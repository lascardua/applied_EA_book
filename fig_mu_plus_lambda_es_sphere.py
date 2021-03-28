# --------------------------------------------------
#      Mu + Lambda ES Algorithm Minimizing a Sphere
# --------------------------------------------------
# file: fig_mu_plus_lambda_es_sphere.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from es_rep.algs.mu_plus_lambda_self_adapt_es \
    import mu_plus_lambda_self_adapt_es
from test_functions_rep.so.sphere import sphere

# 0 - Repeatability
np.random.seed(123)

# 1 - Define the upper and lower bounds of the search space
ndim = 20               # Number of dimensions of the problem
lb = -5*np.ones(ndim)   # Bounds of the search space
ub = 5*np.ones(ndim)

# 2 - Define the parameters for the optimization
maxIterations = 300  # maximum number of iterations
nMC = 10             # number of MC runs

# 3 - Parameters for the algorithm
popsize = 25   # number of individuals in the population
lambd   = 5    # number of children generated at each iteration
theta_0 = np.random.rand(ndim,nMC)  # random initial solution

# 4 - Define the cost function
loss = sphere

# 5 - Run the (mu + lambda) algorithm
best_theta  = np.zeros((ndim,nMC))
best_scores = np.zeros((maxIterations,nMC))
for id_run in range(nMC):
    np.random.seed(123)
    [a, b] = mu_plus_lambda_self_adapt_es(loss,
                                          theta_0[:, id_run],
                                          maxIterations,
                                          lb, ub, popsize, lambd)
    best_theta[:, id_run] = a
    # remove an unused dimension in b
    best_scores[:, id_run] = np.squeeze(b)

# 6 - Plot the convergence curve
from auxiliary.plot_convergence_curve import plot_convergence_curve
fig_file = 'figure_5_6.eps'
title_str = \
    "$(\mu+\lambda)$-ES with Self-adaptation Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,best_scores)


