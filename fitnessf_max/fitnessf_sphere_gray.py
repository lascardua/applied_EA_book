# -------------------------------------------------------------
#                    fitness_sphere_gray
# Computes the fitness value of search point X
# -------------------------------------------------------------
# Inputs:
#   X          - string containing the gray code representation of
#                the search point
#   N          - number of decision variables
#   a and b    - [a, b] interval for the decision variables
#   nbits_word - how many bits are used in the representation of X
# Output:
#   fitness    - fitness value of X
# -------------------------------------------------------------
# file: fitness_sphere_gray.py
# -------------------------------------------------------------
from test_functions_rep.so.sphere import sphere
from encoding_rep.gray2dec import gray2decInterval
from encoding_rep.gen2phen import gen2phen
# -------------------------------------------------------------
def fitness_sphere_gray(X,N,a,b,nbits_word):
    # converts gray-coded X into a decimal number in the interval [a,b]
    Xrv = gen2phen(gray2decInterval, X, N, a, b, nbits_word)
    # calculate the fitness value of Xdv
    fitness_value = -sphere(Xrv)
    return fitness_value

