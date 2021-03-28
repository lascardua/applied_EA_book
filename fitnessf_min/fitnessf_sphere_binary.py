from encoding_rep.gen2phen import gen2phen
from encoding_rep.bin2dec import bin2decInterval
from test_functions_rep.so.sphere import sphere

def fitness_sphere_bin(X,N,a,b,nbits_word):
    # ------------------------------------------------------
    # Calculates the fitness value of search point X for the
    #       minimization of the 2d sphere function
    # ------------------------------------------------------
    # Inputs:
    #   X - string containing the binary representation of
    #       the search point
    #   N - number of phenotypic decision variables
    #   a and b - [a, b] interval
    #   nbits_word - how many bits are used in the
    #                representation of the vector X = [x1, x2]
    # Output:
    #   fitness - fitness value of candidate solution X
    # ------------------------------------------------------

    # Xdv - vector of decision variables in the original
    # domain of the objective function
    Xdv = gen2phen(bin2decInterval, X, N, a, b, nbits_word)
    # Calculate the fitness value of the decision variables
    fitness_value = sphere(Xdv)
    # Return the fitness value
    return fitness_value



