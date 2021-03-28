# -----------------------------------------------------
# Function that repairs a child in case of constraint
# violation. This example only enforces the limits of
# the search space.
# -----------------------------------------------------
# file: repair_child.py
# -----------------------------------------------------
import numpy as np
# -----------------------------------------------------
def f_repair(x,lb,ub):
    # Bound x
    x = np.minimum(x,ub)
    x = np.maximum(x,lb)

    return x





