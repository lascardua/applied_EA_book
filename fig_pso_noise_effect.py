# --------------------------------------------------
#      Effect of Noise on Optimization
# --------------------------------------------------
# file: fig_pso_noise_effect.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from pso_rep.pso import pso
from test_functions_rep.so.griewank import griewank
from sklearn.metrics import mean_squared_error
# --------------------------------------------------
# 1 - Define the upper and lower bounds of the search
#     space
# --------------------------------------------------
ndim = 20               # Number of dimensions
lb = -5*np.ones(ndim)   # Bounds of the search space
ub = 5*np.ones(ndim)

# --------------------------------------------------
# 2 - Define the parameters for the optimization
# --------------------------------------------------
nMC = 20
maxIters = 300  # Number of optimization iterations

# --------------------------------------------------
# 3 - Parameters for the PSO
# --------------------------------------------------
noP = 10        # Number of particles
c1 = np.ones(ndim)  # Cognitive scaling parameter
c2 = np.ones(ndim)  # Social scaling parameter
w_min = 0.4*np.ones(ndim) # Minimum inertia
w_max = 0.9*np.ones(ndim) # Maximum inertia

# --------------------------------------------------
# 4 - Define the cost function
# --------------------------------------------------
# the global minimum of Griewank is
# f(xstar) = 0.0 at xstar = [0,0,...,0]
cost_fun = griewank
x_star = np.zeros(ndim)

def noisy_cost(xx, beta):
    # noise-free value
    y = cost_fun(xx)
    # incorporate noise
    y = y*np.exp(beta*np.random.randn())
    # return the noisy measurement
    return y


# --------------------------------------------------
# fitness function for zero noise
# --------------------------------------------------
def fit_zero(x):
    noise_level = 0
    fit = -noisy_cost(x, noise_level)
    return fit

# --------------------------------------------------
# fitness function for moderate noise
# --------------------------------------------------
def fit_mod(x):
    noise_level = 0.01
    fit = -noisy_cost(x, noise_level)
    return fit

# --------------------------------------------------
# fitness function for high noise
# --------------------------------------------------
def fit_high(x):
    noise_level = 0.05
    fit = -noisy_cost(x, noise_level)
    return fit

# --------------------------------------------------
# 5 - Run the PSO algorithm
# --------------------------------------------------
#  Noiseless Monte Carlo runs
np.random.seed(123) # for repeatability
rmse_nf  = np.zeros(nMC)
for id_run in range(nMC):
    [a, _, _] = pso(fit_zero, maxIters, lb, ub,
                    noP, c1, c2, w_min, w_max)
    rmse_nf[id_run] = mean_squared_error(x_star,a)
# --------------------------------------------------
#  Monte Carlo runs with moderate noise
np.random.seed(123) # for repeatability
rmse_mod  = np.zeros(nMC)
for id_run in range(nMC):
    [a, _, _] = pso(fit_mod, maxIters, lb, ub,
                    noP, c1, c2, w_min, w_max)
    rmse_mod[id_run] = mean_squared_error(x_star,a)
# --------------------------------------------------
#  Monte Carlo runs with high noise
#---------------------------------------------------
np.random.seed(123) # for repeatability
rmse_high  = np.zeros(nMC)
for id_run in range(nMC):
    [a, _, _] = pso(fit_high, maxIters, lb, ub,
                    noP, c1, c2, w_min, w_max)
    rmse_high[id_run] = mean_squared_error(x_star,a)

# --------------------------------------------------
# 6 - BoxPlots
# --------------------------------------------------
data_to_plot = [ rmse_nf , rmse_mod , rmse_high ]
xticklables = ['0','0.01 ','0.05 ']
title = 'Effect of Noise on the Optimization Process of PSO '
xlabel = 'Noise Levels for Griewank '
ylabel = 'RMSE '

import matplotlib.pyplot as plt
bp = plt.boxplot(data_to_plot, notch=0, sym='+', vert=1, whis=1.5)
ticks = np.arange(1,len(xticklables)+1)
plt.xticks(ticks,labels=xticklables)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.yscale('log')
plt.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
plt.title(title)
plt.show()

# change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='k', linewidth=2)


