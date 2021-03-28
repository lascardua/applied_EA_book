# --------------------------------------------------
#      DE Algorithm Minimizing a Noisy Griewank
#               Explicit Averaging
# --------------------------------------------------
# file: fig_de_averaging_noisy_griewank.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from de_rep.algs.de import de
from test_functions_rep.so.griewank import griewank
from sklearn.metrics import mean_squared_error
# --------------------------------------------------
# 1 - Define the upper and lower bounds of the search
#     space
# --------------------------------------------------
ndim = 20               # Number of dimensions of the problem
lb = -5*np.ones(ndim)   # Bounds of the search space
ub = 5*np.ones(ndim)

# --------------------------------------------------
# 2 - Define the parameters for the optimization
# --------------------------------------------------
nMC = 20
maxIters = 300  # Number of optimization iterations

# --------------------------------------------------
# 3 - Parameters for the DE
# --------------------------------------------------
pop_size = 20
step_size=0.8
pc = 0.9

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
# function for performing repeated sampling
# --------------------------------------------------
def repeated_sampling(x, fcost, noise_level, n_repeats):
    fitness = np.zeros(n_repeats)
    # repeated sampling
    for id in range(n_repeats):
        fitness[id] = fcost(x,noise_level)
    # calculate the mean value of the samples
    mean_fit = np.mean(fitness)
    # return the mean value
    return mean_fit

# --------------------------------------------------
# Cost function for 1 evaluation
# --------------------------------------------------
def cost_1(x):
    n_repeats = 1
    noise_level = 0.05
    fit = repeated_sampling(x, noisy_cost, noise_level,
                            n_repeats)
    return fit

# --------------------------------------------------
# Cost function for 4 evaluations
# --------------------------------------------------
def cost_4(x):
    n_repeats = 4
    noise_level = 0.05
    fit = repeated_sampling(x, noisy_cost, noise_level,
                            n_repeats)
    return fit

# --------------------------------------------------
# Cost function for 8 evaluations
# --------------------------------------------------
def cost_8(x):
    n_repeats = 8
    noise_level = 0.05
    fit = repeated_sampling(x, noisy_cost, noise_level,
                            n_repeats)
    return fit

# --------------------------------------------------
# 5 - Run the DE algorithm
# --------------------------------------------------
# --------------------------------------------------
# 1 evaluation
# --------------------------------------------------
np.random.seed(123)
rmse_1_reps  = np.zeros(nMC)
for id_run in range(nMC):
    [a, _] = de(cost_1, pop_size, maxIters, pc, lb, ub,
                step_size)
    rmse_1_reps[id_run] = mean_squared_error(x_star,a)

# --------------------------------------------------
# 4 evaluations
# --------------------------------------------------
np.random.seed(123)
rmse_4_reps  = np.zeros(nMC)
for id_run in range(nMC):
    [a, _] = de(cost_4, pop_size, maxIters, pc, lb, ub,
                step_size)
    rmse_4_reps[id_run] = mean_squared_error(x_star,a)

# --------------------------------------------------
# 8 evaluations
# --------------------------------------------------
np.random.seed(123)
rmse_8_reps  = np.zeros(nMC)
for id_run in range(nMC):
    [a, _] = de(cost_8, pop_size, maxIters, pc, lb, ub,
                step_size)
    rmse_8_reps[id_run] = mean_squared_error(x_star,a)

# --------------------------------------------------
# 6 - Boxplot
# --------------------------------------------------
data_to_plot = [ rmse_1_reps , rmse_4_reps , rmse_8_reps ]
xticklables = ['1','4','8']
title = 'Effect of Explicit Averaging on the DE Optimization of Noisy Griewank '
xlabel = 'Number of Evaluations '
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