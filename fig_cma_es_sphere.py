# --------------------------------------------------
#      CMA-ES Algorithm Minimizing a Sphere
#              fig_cma_es_sphere.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
import matplotlib.pyplot as plt
from es_rep.algs.cmaes import cmaes
from test_functions_rep.so.sphere import sphere
# --------------------------------------------------
# Plot the convergence curve
# --------------------------------------------------
def plot_convergence_curve(fig_name,title_str,fbest_h,
                           fig_size_x = 8,fig_size_y = 4,
                           dpi=1000):
    num_vals = len(fbest_h)
    t = np.linspace(0, num_vals-1, num_vals)
    fig, ax = plt.subplots(figsize=(fig_size_x,fig_size_y),
                           dpi=dpi) # figura 800x600 pixels
    ax.plot(t, fbest_h,c='0.35')
    #ax.set_xlabel(r'$\mathit{iteration}$', fontsize=18)
    #ax.set_ylabel(r'$f_o$', fontsize=18)
    ax.set_xlabel(r'$\mathit{iteration}$')
    ax.set_ylabel(r'$f_o$')
    ax.set_title(title_str)
    ax.grid(True)
    plt.savefig(fig_name,format="eps",dpi=dpi)
# --------------------------------------------------
# Minimization
# --------------------------------------------------
# Repeatability
np.random.seed(123)

# 1 - Define the upper and lower bounds of the search space
ndim = 20               # Number of dimensions of the problem
ubc = 5
lbc = -5
lb = lbc*np.ones(ndim)     # lower bound for the search space
ub = ubc*np.ones(ndim)   # upper bound for the search space

# 2 - Define the parameters for the optimization
maxIterations = 300  # maximum number of iterations
nMC = 10             # number of MC runs
# 3 - Parameters for the algorithm
sigma_0 = 0.3*(ubc - lbc)
theta_0 = np.random.rand(ndim,nMC)  # random initial solution

# 4 - Define the cost function
fcost = sphere

# 5 - Run the CMAES algorithm
best_theta  = np.zeros((ndim,nMC))
best_scores = np.zeros((maxIterations,nMC))
for id_run in range(nMC):
    np.random.seed(123)
    [a, b] = cmaes(fcost, theta_0[:, id_run], sigma_0, maxIterations)
    best_theta[:, id_run] = a
    best_scores[:, id_run] = np.squeeze(b) # remove an unused dimension in b

# Plot the convergence curves--------------------------
fig_file = 'figure_5_9.eps'
title_str = "CMA-ES Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,best_scores)


