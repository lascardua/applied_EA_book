from test_functions_rep.so.ackley import ackley
# -----------------------------------------------
#  Minimization of the Real-Valued Ackley Function
# -----------------------------------------------
def fitness_ackley_rv(X):
    fitness = -ackley(X)
    return fitness





