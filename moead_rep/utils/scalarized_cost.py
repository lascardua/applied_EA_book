# -----------------------------------------------------
# Tchebycheff scalarized cost function
# -----------------------------------------------------
# fc    - value of the multi-objective cost function for
#         a given individual
# z     - reference point
# lambd - weight vector
# -----------------------------------------------------
# file: scalarized_cost.py
# -----------------------------------------------------
import numpy as np
# -----------------------------------------------------
def scalarized_cost(fc, z, lambd):
    g = np.max(lambd * np.abs(fc - z))
    return g