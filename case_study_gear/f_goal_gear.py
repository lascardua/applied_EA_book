# --------------------------------------------------
# Objective Function for the Multi-Objective  Gear
# Train Problem
# --------------------------------------------------
# file: f_goal_gear.py
# --------------------------------------------------
import numpy as np
# --------------------------------------------------
def f_Gear(x):
    f1 = (1 / 6.931 - (x[0] * x[1]) / (x[2] * x[3]))** 2
    f2 = np.max(x)
    f = np.array([f1, f2])
    return f