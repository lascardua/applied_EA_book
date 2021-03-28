# -----------------------------------------------
#  Minimization of the G08 Function
# For Maximization Algorithms, like the GA
# -----------------------------------------------
from test_functions_rep.so.g08 import g08
# -----------------------------------------------
def fitness_g08(x):
    # barrier functions to enforce the search domain limits
    if x[0]<=0 or x[0]>10:
        f = 100
        return -f
    if x[1]<0 or x[1]>10:
        f = 100
        return -f
    # goal function
    f,g1,g2 = g08(x)
    # barrier function to enforce inequality constraints
    if g1>0 or g2>0:
        f = 100
    # for minimization by algorithms that perform
    # maximization
    f = -f
    return f