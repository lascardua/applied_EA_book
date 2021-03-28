# -----------------------------------------------------
# Function that repairs a child in case of constraint
# violation. This example only enforces the limits of
# the search space.
# -----------------------------------------------------
# file: repair_child.py
# -----------------------------------------------------
import numpy as np
# -----------------------------------------------------
# def f_repair(x,lb,ub):
#     # Bound x
#     x = np.minimum(x,ub)
#     x = np.maximum(x,lb)
#     return x


from de_rep.algs.de import de
from moead_rep.utils.scalarized_cost import scalarized_cost

def f_repair(f_cost,x,z,lambd,lb,ub):
    max_iters = 10
    pop_size = 10
    pc = 0.9

    def de_cost(x, z = z, lambd = lambd):
        fc = f_cost(x)
        y = scalarized_cost(fc, z, lambd)
        return y

    x_de, cost_de = de(de_cost, pop_size, max_iters, pc, lb, ub, step_size=0.8, theta_0 = x)

    if de_cost(x) < de_cost(x_de):
        return x
    else:
        return x_de



