# --------------------------------------------------------------
# Compute the critical values of the Student's t distribution
# --------------------------------------------------------------
# N     - number of samples
# gamma - confidence level
# --------------------------------------------------------------
# file: compute_critical_values_student_t.py
# --------------------------------------------------------------
from scipy.stats import t as t_dist
# --------------------------------------------------------------
def critical_values_t(N, gamma):
    # 1 - Number of degrees of freedom and probability p
    p       = (1 - gamma) / 2.0     # tail probability
    nDof    = N - 1                 # degrees of freedom

    # 2 - Compute the lower critical value, cl, # such that
    #     P(Z <= cl) = pl
    # Compute the probability pl for using with the ppf function
    pl = p
    # Compute the value of the lower critical point using the
    # percent point function (inverse of cdf)
    cl = t_dist.ppf(pl, nDof)
    # Print
    print('cl = {}'.format(cl))

    # 4 - Compute the upper critical value, cu, such that
    #     P(Z >= cu) = pu
    # Compute the probability pu for using with the ppf function
    pu = 1 - p
    # Compute the value of the lower critical point using the
    # percent point function (inverse of cdf)
    cu = t_dist.ppf(pu, nDof)
    print('cu = {}'.format(cu))

    return cl, cu
