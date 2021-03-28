# -----------------------------------------------
#  Fitness for the real-valued sphere function
# -----------------------------------------------
# Input:
#   X   - real-valued chromosome
# Output:
#   F   - f(X)
# -----------------------------------------------
# file: fitness_sphere_rv.py
# -----------------------------------------------
from test_functions_rep.so.sphere import sphere
# -----------------------------------------------
def fitness_sphere_rv(X):
    fitness = -sphere(X)
    return fitness
