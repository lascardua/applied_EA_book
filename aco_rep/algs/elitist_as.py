# --------------------------------------------------
#               elitist_AS
#   Class that implements the elitist_AS algorithm "elitist
#   ant system" version
# --------------------------------------------------
# Inputs:
#   graph               - Graph of the TSP problem
#   start_node          - Start node for all ants
#   n_ants              - Number of ants
#   n_best              - number of elite solutions
#   n_iterations        - Number of optimization iterations
#   rho                 - pheromone evaporation rate
#   alpha               - importance of the distance between cities
#   beta                - importance of the pheromone trail
#   w                   - weight for the extra pheromone deposit
#                         for elite solutions
# Outputs:
#   all_time_cheapest_path - shortest path found
# --------------------------------------------------
#   Implemented as a minimization algorithm
# --------------------------------------------------
# file: elitist_as.py
# --------------------------------------------------
import numpy as np
from aco_rep.algs.ant import Ant
# --------------------------------------------------
class elitist_AS(object):
    def __init__(self, graph, start_node, n_ants, n_best, n_iterations, rho, alpha, beta, w):
        self.graph = graph
        self.costs = graph.cost_matrix
        self.start_node = start_node
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        self.w    = w
        # uniform distribution of pheromones
        self.pheromone_matrix = np.ones(self.costs.shape)
    # --------------------------------------------------
    # Perform the optimization
    # --------------------------------------------------
    def run(self):
        # storage for the all-time best solution
        all_time_cheapest_path = [[], np.inf]
        for i in range(self.n_iterations):
            # generate candidate solutions
            candidate_sols = self.gen_candidate_solutions()
            # decay pheromone level on all edges
            self.pheromone_matrix = (1-self.rho)* \
                    self.pheromone_matrix
            # add pheromone to the arcs that comprise all
            # candidate solutions
            self.update_pheromone(candidate_sols,
                    self.n_ants, w = 1.0)
            # reinforce pheromone on the arcs that comprise
            # the elite candidate solutions
            self.update_pheromone(candidate_sols,
                    self.n_best, w = self.w)
            # find the candidate solution with best cost
            cheapest_path = min(candidate_sols,
                                key=lambda x: x[1])
            # update the best solution found so far
            if cheapest_path[1] < all_time_cheapest_path[1]:
                all_time_cheapest_path = cheapest_path
        # return the best solution found
        return all_time_cheapest_path
    # --------------------------------------------------
    # Update the pheromone intensity for the paths that
    # comprise candidate solutions
    # --------------------------------------------------
    def update_pheromone(self, candidate_sols, n_sols,w):
        # sort paths in ascending order of path cost
        sorted_paths = sorted(candidate_sols, key=lambda x: x[1])
        # the pheromone trail is updated only for
        # the n_sols paths
        for path, dist in sorted_paths[:n_sols]:
            # for each edge in the path
            for edge in path:
                # update the pheromone quantity
                self.pheromone_matrix[edge] = \
                    self.pheromone_matrix[edge] + \
                    (w / self.costs[edge])
    # --------------------------------------------------
    # Generate one candidate solution for each ant
    # --------------------------------------------------
    def gen_candidate_solutions(self):
        all_paths = []
        # for each ant
        for i in range(self.n_ants):
            ant = Ant(start_node=self.start_node,
                      graph = self.graph,
                      pheromone_matrix = self.pheromone_matrix,
                      alpha = self.alpha, beta = self.beta)
            # generate a round-trip path
            # starting in the first node
            path = ant.gen_path()
            # add the round-trip path to
            # the set of candidate soutions
            all_paths.append((path,
                     self.graph.calc_path_cost(path)))
        # returns the set of new candidate solutions
        return all_paths





