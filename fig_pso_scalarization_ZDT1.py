# --------------------------------------------------
#        Scalarization Method Using the PSO Algorithm
#            to Minimize the ZDT1 Function
# --------------------------------------------------
# file: fig_pso_scalarization_ZDT1.py
# --------------------------------------------------
import numpy as np
from pso_rep.pso import pso
from test_functions_rep.mo.zdt1 import zdt1

# 1 - Define the upper and lower bounds of the search
#     space
lb = np.array([0, 0])
ub = np.array([1, 1])

# 2 - Define the parameters for the optimization
noP = 30        # number of particles
maxIters = 50   # number of optimization iterations
ndim = 2        # number of dimensions of the problem
z_star = np.array([0.5, 0.25]) # ideal point

# 3 - Parameters for the PSO algorithm
c1 = np.ones(ndim)  # cognitive scaling parameter
c2 = np.ones(ndim)  # social scaling parameter
w_min = 0.2*np.ones(ndim) # maximum inertia
w_max = 0.9*np.ones(ndim) # minimum inertia


# 4 - Define the fitness function
# arbitrary non-negativeweights
lambd = np.ones(ndim)
# fitness function returns the negative of
# the weighted Chebyshev distance
def ffit(x):
    # Calculate the value of zdt1 at x
    z = zdt1(x)
    # Calculate the weighted Chebyshev distance.
    # The minus sign is due to PSO be
    # a maximization algorithm
    dist = -np.max(lambd * np.abs(z - z_star))
    return dist


# 5 - Run the PSO algorithm
xbest, _, _ = pso(ffit, maxIters, lb, ub, noP,
                     c1, c2, w_min, w_max)

# Obtaining the point in the
# objective space that
# corresponds to xbest
fbest = zdt1(xbest)

# print the results
print('xbest: {}'.format(xbest))
print('fbest: {}'.format(fbest))


# Plot the Pareto Front and the solution found by PSO
from auxiliary.read_ZDT1_PF import read_zdt1_pf
true_pf = read_zdt1_pf()
import matplotlib.pyplot as plt
plt.xlabel('$f_1$', fontsize=15)
plt.ylabel('$f_2$', fontsize=15)
plt.scatter(z_star[0], z_star[1], marker="*", color='k', label='$\mathbf{z}^{\star}$')
plt.scatter(fbest[0], fbest[1], marker="o", color='k', label='PSO solution')
plt.plot(true_pf[:,0],true_pf[:,1], color='0.5',label='True Pareto Front')
plt.title('PSO Solving ZDT1 by Scalarization')
plt.legend()
plt.grid()
plt.xlim(0,1)


# Print figure
fig_name =  'figure_10_10.eps'

from auxiliary.save_fig import save_fig
save_fig(fig_name)