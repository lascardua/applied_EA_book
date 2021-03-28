# --------------------------------------------------------------
# Compute a 95% confidence interval for the mean value of
# normally distributed data with UNknown variance
# --------------------------------------------------------------
import numpy as np
from scipy.stats import t as t_dist
# --------------------------------------------------------------

# 1 - Define the confidence level and the number of samples
sigma = 0.95        # confidence level
N = 10              # number of samples

# 2 - Number of degrees of freedom and probability p
p = (1 - sigma)/2.0 # probability p
nDof = N -1         # degrees of freedom

# 3 - Compute the lower critical value, cl, such that P(Z <= cl) = pl
# Compute the probability pl for using with the ppf function
pl = p
# Compute the value of the lower critical point using the
# percent point function (inverse of cdf)
cl = t_dist.ppf(pl, nDof)
# Print
print('cl = {}'.format(cl))

# 4 - Compute the upper critical value, cu, such that P(Z >= cu) = pu
# Compute the probability pu for using with the ppf function
pu = 1 - p
# Compute the value of the lower critical point using the
# percent point function (inverse of cdf)
cu = t_dist.ppf(pu, nDof)
print('cu = {}'.format(cu))

# 5 - Normally distributed samples
delta =  0.1
np.random.seed(123)                # for repeatability
X = np.random.normal(5,delta,N)    # generate N samples
print('X is {}'.format(X))

# 6 - Compute the sample mean and sample standard deviation
Xbar = np.mean(X)                    # sample mean
print('Xbar = {}'.format(Xbar))
S =  np.sqrt((1/(N-1))*np.sum((X - Xbar)**2)) # sample sd
print('S = {}'.format(S))

# 6 - Confidence Interval
lb = Xbar - cu*(S/np.sqrt(N))       # lower bound of the CI
ub = Xbar - cl*(S/np.sqrt(N))       # upper bound of the CI

print('the {}% CI is [{},{}]'.format(sigma*100,lb,ub))