# --------------------------------------------------
#                G08
# Implements the 2-dimensional G08 function
# --------------------------------------------------
# file: g08.py
# --------------------------------------------------
import math as m
# --------------------------------------------------
def g08(x):
    f = -(m.sin(2 * m.pi * x[0]) ** 3) * \
        (m.sin(2 * m.pi * x[1])) / ((x[0] ** 3) * (x[0] + x[1]))
    g1 = x[0] ** 2 - x[1] + 1 # g1 <= 0
    g2 = 1 - x[0] + (x[1] - 4) ** 2 # g2 <= 0
    return f, g1, g2