# --------------------------------------------------
# Graph - class that implements the graph where the
# search occurs
# --------------------------------------------------
# file: graph.py
# --------------------------------------------------
class Graph(object):
    def __init__(self, cost_matrix):#, rank: int):
        self.cost_matrix = cost_matrix
        self.n_nodes = len(cost_matrix)

    # calculate the cost of a given solution
    def calc_path_cost(self, path):
        total_cost = 0
        for edge in path:
            total_cost += self.cost_matrix[edge]
        return total_cost

