# --------------------------------------------------
#         elitist_AS Solves TSP with 4 Cities
# --------------------------------------------------
# file: run_elitist_as_4_cities.py
# --------------------------------------------------

import numpy as np
from aco_rep.algs.elitist_as import elitist_AS
from aco_rep.graph import Graph

# 1 - Write the matrix of costs
# The cost of going from a city to herself
# is infinite, meaning that  there is no
# edge linking a city to herself
cost_matrix = np.array([[np.inf, 9, 11, 7],
                      [9, np.inf, 15, 5],
                      [11, 15, np.inf, 4],
                      [7, 5, 4, np.inf]])

# 2 - Instantiate the graph
graph = Graph(cost_matrix=cost_matrix)
# 3 - Instantiate the elitist_AS
node_0 = 0      # start at city A (Python starts enumerating with zero)
n_ants = 20     # number of antes
n_best = 2      # number of best candidate solutions that get
                # extra pheromone deposit
w = 0.1         # weight for the extra pheromone deposit on
                # the paths of the elite solutions
n_gen = 50      # number of generations of ants
rho = 0.5       # pheromone evaporation rate
alpha = 0.5     # importance of pheromone level on an edge on an
                # ant's decision to pick the path
beta = 0.5      # importance of the cost of an edge on an ant's
                # decision to pick the path
aco = elitist_AS(graph, node_0, n_ants, n_best, n_gen,
                 rho, alpha=alpha, beta=beta, w = w)
# 4 - Solve the problem
shortest_path = aco.run()
# 5 - Print the results
print ("shorted_path: {}".format(shortest_path))








