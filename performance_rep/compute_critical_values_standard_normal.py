# --------------------------------------------------------------
# Compute and print the critical values of a standard normal
# --------------------------------------------------------------
# gamma - confidence level
# --------------------------------------------------------------
# file: compute_critical_values_standard_normal.py
# --------------------------------------------------------------
from scipy.stats import norm as rv
# --------------------------------------------------------------
def critical_values_standard_normal(gamma):
    # 1 - Define the tail probability
    p = (1 - gamma)/2.0

    # 2 - Compute the lower critical value, cl, such that P(Z <= cl) = pl
    # Compute the probability pl for using with the ppf function
    pl = p
    # Compute the value of the lower critical point using the
    # percent point function (inverse of cdf)
    cl = rv.ppf(pl, loc =0, scale = 1)
    # Print
    print('cl = {}'.format(cl))

    # 3 - Compute the upper critical value, cu, such that P(Z >= cu) = pu
    # Compute the probability pu for using with the ppf function
    pu = 1 - p
    # Compute the value of the lower critical point using the
    # percent point function (inverse of cdf)
    cu = rv.ppf(pu, loc =0, scale = 1)
    print('cu = {}'.format(cu))

    return cl, cu
