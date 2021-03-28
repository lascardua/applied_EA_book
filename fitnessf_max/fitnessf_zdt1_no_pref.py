#--------------- Fitness function -------------------------
# Minimization of the ZDT1 Function Using the No-Preference
# Method
#------------------------------------------------------------
# file: fitnessf_zdt1_no_pref.py
#------------------------------------------------------------
from test_functions_rep.mo.zdt1 import zdt1
from encoding_rep.euclidean_dist import euclidean_dist
#------------------------------------------------------------
def fitnessf_zdt1_no_pref(x, z_ideal):
    # Calculate the value of zdt1 at x
    z = zdt1(x)
    # Calculate the distance
    dist = -euclidean_dist(z,z_ideal)
    return dist