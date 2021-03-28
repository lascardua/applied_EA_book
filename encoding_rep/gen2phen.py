# ------------------------------------------------------
#   Converts binary coded array X into N decimal decision
#                variables in [a,b]
# ------------------------------------------------------
# Inputs:
#   disc2decf --> bin2decInterval for binary
#                 representation
#             --> gray2decInterval for gray-coded
#                 representation
#   X - vector containing the discrete representation of
#       the array of decision variables
#   N - number of phenotypic decision variables
#   a, b - [a, b] interval for the phenotype decision
#          variables
#   nbits_word - number of bits used in the discrete
#                representation of the vector of decision
#                variables
# Output:
#   Xdv - array of phenotypic decision variables
# ------------------------------------------------------
# file: gen2phen.py
# ------------------------------------------------------
import numpy as np
def gen2phen(disc2decf,X,N,a,b,nbits_word):
    # nbits_dv - number of bits for each decision variable
    nbits_dv = int(nbits_word / N)
    inii = 0 # initial pointer for slicing X
    endi = nbits_dv # final pointer for slicing X
    Xdv = np.zeros(N) # array of decimal decision variables
    for ii in range(N):
        # binary representation of the ith decision variable
        bxdv = X[inii:endi]
        # convert bxdv to string
        xstr = np.array2string(bxdv, separator='')
        # remove the delimiting square brackets from xstr
        xstr = xstr[1:nbits_dv + 1]
        # convert from binary to decimal in the interval [a,b]
        dnum = disc2decf(xstr, a[ii], b[ii], nbits_dv)
        # store in the array of decision variables
        Xdv[ii] = dnum
        # update the pointers for the next iteration
        inii = endi
        endi = endi + nbits_dv
    return Xdv