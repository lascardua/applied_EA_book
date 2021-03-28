# ---------------------------------------------------
#            general_mutation
# Perform a general mutation on an individual
# ---------------------------------------------------
# Inputs:
#  theta - individual
#  cov   - covariance matrix of the mutation
# Outputs:
#  theta - mutated individual
# ---------------------------------------------------
# file: mutation_general.py
# ---------------------------------------------------
import numpy as np
# ---------------------------------------------------
def general_mutation(theta, cov):
    # dimensionality
    nVar = np.shape(theta)[0]
    # perform mutation
    theta = theta + np.random.multivariate_normal(np.zeros(nVar), cov)
    # return mutated individual
    return theta