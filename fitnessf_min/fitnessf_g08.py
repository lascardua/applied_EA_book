from test_functions_rep.so.g08 import g08
# -----------------------------------------------
#  Minimization of the G08 Function
# For Minimization Algorithms, like the ES
# -----------------------------------------------
def fitness_g08(x):
    if x[0] <= 0 or x[0] > 10:
        f = 100
        return f
    if x[1] < 0 or x[1] > 10:
        f = 100
        return f
        # goal function
    f, g1, g2 = g08(x)
    # barrier function to enforce inequality constraints
    if g1 > 0 or g2 > 0:
        f = 100
    return f