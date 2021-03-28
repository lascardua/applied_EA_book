# --------------------------------------------------------------
# Performance assessment on the minimization of a noiseless
# function. The samples are assumed to be Gaussian with unknown
# variance.
# --------------------------------------------------------------
# file: assessment_performance_GAc_noiseless.py
# --------------------------------------------------------------
import numpy as np
from performance_rep.compute_critical_values_student_t import \
    critical_values_t
from performance_rep.so_monte_carlo_runs import \
    perform_MC_runs
from fitnessf_max.fitnessf_griewank_rv import \
    fitness_griewank_rv, griewank
# --------------------------------------------------------------
# 1 - Define the confidence level and the number of samples
sigma   = 0.95    # confidence level
N       = 40      # number of samples

# 2 - Compute the critical values of the t distribution
[cl,cu] = critical_values_t(N,sigma)

# 3 - Define the test problem and its optimal solution
# Define the upper and lower bounds of the search space
n_dim   = 2  # Number of dimensions of the problem
ubc     = 5
lbc     = -5
lb      = lbc * np.ones(n_dim)  # Lower bound for the
                                # search space
ub      = ubc * np.ones(n_dim)  # Upper bound for the
                                # search space
x_star    = np.zeros(n_dim)     # optimal solution
# Define the fitness function
fitness_f = fitness_griewank_rv # fitness function
test_f    = griewank            # test function


# 3 - Perform the Monte Carlo runs
est_solutions = perform_MC_runs(fitness_f,
                                n_dim, lb,
                                ub, N)

# Compute the best scores produced by the GA
best_scores = np.zeros(N)
for i in range(N):
    best_scores[i] = test_f(est_solutions[i])

# 4 - Compute the estimation errors
X = np.abs(best_scores - test_f(x_star))

# 5 - Compute the sample mean and sample standard
#     deviation
Xbar = np.mean(X)   # sample mean
print('Xbar = {}'.format(Xbar))
S = np.std(X)       # sample sd
print('S = {}'.format(S))

# 6 - Compute the confidence Interval
lb = Xbar - cu * (S / np.sqrt(N))  # lower bound of
                                   # the CI
ub = Xbar - cl * (S / np.sqrt(N))  # upper bound of
                                   # the CI
print('the {}% CI is [{},{}]'.format(sigma * 100, lb, ub))


