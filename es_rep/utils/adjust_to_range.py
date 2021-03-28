# ---------------------------------------------------
#               es_adjust_to_range
# Trim an individual so it stays within allowed limits
# ---------------------------------------------------
# theta - individual
# theta_min - lower bound
# theta_max - upper bound
# ---------------------------------------------------
import numpy as np
# ---------------------------------------------------
def es_adjust_to_range(theta, theta_min, theta_max):
    theta = np.maximum(theta, theta_min)
    theta = np.minimum(theta, theta_max)
    return theta