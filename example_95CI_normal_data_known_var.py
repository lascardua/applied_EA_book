# --------------------------------------------------------------
# Compute a 95% confidence interval for the mean value of
# normally distributed data with known variance
# --------------------------------------------------------------
# file: example_95CI_normal_data_known_var.py
# --------------------------------------------------------------
import numpy as np
from performance_rep.compute_critical_values_standard_normal \
    import critical_values_standard_normal
# --------------------------------------------------------------
# 1 - Define the confidence level
gamma = 0.95

# 2 - Compute the critical levels
[cl, cu] = critical_values_standard_normal(gamma)

# 3 - Generate normally distributed samples
delta = 0.1
N     = 10
np.random.seed(123)                # for repeatability
X = np.random.normal(5,delta,N)    # generate N samples
print('X is {}'.format(X))

# 5 - Confidence Interval
Xbar = np.mean(X)                   # mean of the samples
print('Xbar = {}'.format(Xbar))
lb = Xbar - cu*(delta/np.sqrt(N))   # lower bound of the CI
ub = Xbar - cl*(delta/np.sqrt(N))   # upper bound of the CI

print('the {}% CI is [{},{}]'.format(gamma*100,lb,ub))