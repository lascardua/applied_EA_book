
# -----------------------------------------------
#        Fitness Griewank real-Valued
# -----------------------------------------------
# Fitness function for algorithms that perform
# maximization in a real-valued search space
# -----------------------------------------------
# file: fitness_griewank_rv.py
# -----------------------------------------------
from test_functions_rep.so.griewank import griewank
# -----------------------------------------------
def fitness_griewank_rv(X):
    fitness = -griewank(X)
    return fitness
