# -----------------------------------------------------
# Initialize weight vectors and the corresponding
# neighborhoods
# -----------------------------------------------------
# nGoals        - number of goals
# popSize       - population size
# T             - number of neighbors
# -----------------------------------------------------
# initialize_L_B.py
# -----------------------------------------------------
import numpy as np
from scipy.spatial.distance import cdist
# -----------------------------------------------------
def initialize_lambda_neighbors(popSize, T, nGoals):
    # 1 - Compute the lambda vectors
    # # There are popSize lambda vectors
    # # each lambda vector has nGoals elements
    lambdas = np.zeros((popSize, nGoals))
    for il in range(popSize):
        lambdas[il] = np.random.rand(nGoals)
    # 2 - Compute neighborhoods
    subProblem_ids_neighbors = np.zeros((popSize, T), dtype=int)
    # Compute distances between weight vectors
    D = cdist(lambdas,lambdas)
    # Compute the T nearest neighbors of each weight vector
    for i in range(popSize):
        inds = np.argsort(D[i,:])
        # Start at 1 in order to prevent the ith element from
        # being its own neighbor
        subProblem_ids_neighbors[i] = inds[1:T+1]
    return lambdas, subProblem_ids_neighbors
