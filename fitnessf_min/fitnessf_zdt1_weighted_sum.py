#--------------- Fitness function -------------------------
#         Weighted Sum A Priori Method
# fitnessf_zdt1_weighted_sum.py
# ----------------------------------------------------------
from fitnessf_rep.zdt1 import zdt1   # Import the zdt1 function
w = [0.7, 0.3] # define the weights
# Measures the Euclidean distance between y=zdt1(x)
# and the ideal point
def fitnessf_zdt1_weighted_sum(x,w=w):
    if sum(w)>1:
        print('the sum of the weights must me equal to 1')
        exit()
    z = zdt1(x) # Calculate the value of zdt1 at x
    wsum = w[0]*z[0] + w[1]*z[1] # weighted sum
    return wsum