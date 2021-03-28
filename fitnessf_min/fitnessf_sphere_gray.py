from test_functions_rep.so.sphere import sphere
from encoding_rep.gray2dec import gray2decInterval
from encoding_rep.gen2phen import gen2phen

def fitness_sphere_gray(X,N,a,b,nbits_word):
    # fitness_sphere_gray - Calculates the fitness value of search point X for the minimization of the 2d sphere function
    # Inputs:
    #   X - string containing the gray code representation of the search point
    #   N - number of phenotypic decision variables
    #   a and b - [a, b] interval
    #   nbits_word - how many bits are used in the representation of the vector X = [x1, x2]
    # Output:
    #   fitness - fitness value of candidate solution X

    Xdv = gen2phen(gray2decInterval, X, N, a, b, nbits_word)
    fitness_value = sphere(Xdv) # calculate the fitness valueof the decision variables
    return fitness_value

