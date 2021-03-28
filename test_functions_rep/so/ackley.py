import numpy as np
def ackley(xx):
    # INPUTS:
    # xx = [x1, x2, ..., xd]
    # a = constant (optional), with default value 20
    # b = constant (optional), with default value 0.2
    # c = constant (optional), with default value 2*pi
    #
    # Global minimum f(x^{\star})=0 at x^{\star}=[0,0,...,0];
    d = len(xx)
    c = 2*np.pi
    b = 0.2
    a = 20

    sum1 = 0
    sum2 = 0
    for ii in range(d):
        xi = xx[ii]
        sum1 = sum1 + xi**2
        sum2 = sum2 + np.cos(c*xi)

    term1 = -a * np.exp(-b*np.sqrt(sum1/d))
    term2 = -np.exp(sum2/d)

    y = term1 + term2 + a + np.exp(1)
    return y