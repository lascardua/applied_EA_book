#--------------- Fitness function -------------------------
# Minimization of the ZDT1 Function Using the No-Preference
# Method
# fitnessf_zdt1_no_pref.py
#------------------------------------------------------------
import numpy as np
from test_functions_rep.mo.zdt1 import zdt1   # Import the zdt1 function
from encoding_rep.euclidean_dist import euclidean_dist   # Import the euclidean
                                            # distance function

z_ideal = np.array([ 0.1 , 0.5 ])           # Define an ideal point
# Measures the Euclidean distance between y=zdt1(x)
# and the ideal point
def fitnessf_zdt1_no_pref(x,z_ideal=z_ideal):
    z = zdt1(x) # Calculate the value of zdt1 at x
    dist = euclidean_dist(z,z_ideal) # Minus for minimization
    return dist