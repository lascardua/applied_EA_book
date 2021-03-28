# --------------------------------------------------------------
# Performance assessment on the minimization of a noiseless
# function. The samples are assumed to be Gaussian with unknown
# variance.
# --------------------------------------------------------------
# file: assessment_performance_NSGA2_noiseless.py
# --------------------------------------------------------------
import numpy as np
from nsga_rep.algs.nsga2 import nsga2
from auxiliary.init_rv import init_rv
from test_functions_rep.mo.zdt1 import zdt1
from performance_rep.compute_critical_values_student_t import \
    critical_values_t
from operators_rep.crossover.crossover_rv_sbx import \
    sbx_crossover
from operators_rep.mutation.mutation_polynomial_rv import \
    mutation_polynomial_rv
# -------------------------------------------------------------
# Compute the IDG metric
# -------------------------------------------------------------
def calc_IDG_metric(true_pf, approx_PF):
    from scipy.spatial.distance import euclidean
    normZ = len(true_pf)
    normA = len(approx_PF)

    # IGD
    dist = np.zeros((normZ, normA))
    for idz in range(normZ):
        for ida in range(normA):
            dist[idz, ida] = euclidean(true_pf[idz], approx_PF[ida])
    idg = 0
    for idz in range(normZ):
        idg = idg + np.min(dist[idz])
    idg = (1 / normZ) * idg
    return idg
# -------------------------------------------------------------
# Generate the true PF of ZDT1
# -------------------------------------------------------------
def generate_zdt1_pf():
    # define the number of points to be generated
    n_samples = 1000
    # by definition, we have f1 = x_1
    x1 = np.linspace(0, 1, n_samples)
    f1 = x1
    # at the front, we have g(x_2, ..., x_n) = 1,
    # thus f2 = 1 - np.sqrt(f1)
    f2 = 1 - np.sqrt(f1)
    pareto_front = np.array([f1, f2]).T
    return pareto_front
# --------------------------------------------------------------
# MC runs
# --------------------------------------------------------------
def perform_MC_runs(cost_f, true_pf, n_dim, n_goals, lb, ub, nMC):
    # 1 - Define the parameters of the optimization
    npop = 200            # Number of individuals in the population
    maxIterations = 500    # Maximum number of iterations

    # 2 - Parameters for the algorithm
    pc          = 0.9        # Crossover probability
    pm          = 1/n_dim        # Mutation probability

    init_f      = init_rv                   # Creates the initial population
    crossover_f = sbx_crossover             # Implements crossover
    mutation_f  = mutation_polynomial_rv    # Implements mutation

    # 3 - Run the NSGA2 algorithm
    IGD         = np.zeros(nMC) # Store IGD values
    np.random.seed(123)                 # For repeatability
    for id_MC in range(nMC):            # Monte Carlo runs
        approx_PF, _  = nsga2(npop, maxIterations, pc, pm,
                      init_f,
                      cost_f,
                      crossover_f,
                      mutation_f,
                      lb, ub, n_dim, n_goals)

        IGD[id_MC] = calc_IDG_metric(true_pf, approx_PF)
    # Return the solutions found
    return IGD
# --------------------------------------------------------------
#  Assessing the performance
# --------------------------------------------------------------
# 1 - Define the confidence level and the number of samples
sigma   = 0.95    # confidence level
N       = 40      # number of samples

# 2 - Compute the critical values of the t distribution
[cl,cu] = critical_values_t(N,sigma)

# 3 - Define the test problem and its optimal solution
f_name = 'ZDT1'
n_dim = 30
f_cost = zdt1
n_goals = 2
ubc = 1
lbc = 0
lb = lbc * np.ones(n_dim)  # Lower bound for the
# search space
ub = ubc * np.ones(n_dim)  # Upper bound for the
# search space
true_PF = generate_zdt1_pf()

# 4 - Perform the Monte Carlo runs
X = perform_MC_runs(f_cost,
                       true_PF,
                       n_dim,
                       n_goals,
                       lb,
                       ub,
                       N)

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


