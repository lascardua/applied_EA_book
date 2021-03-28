from test_functions_rep.so.rosenbrock import rosenbrock
# -----------------------------------------------
#  Minimization of the Real-Valued Rosenbrock Function
# -----------------------------------------------
def fitness_rosenbrock_rv(X):
    fitness = -rosenbrock(X)
    return fitness





