# ---------------------------------------------------
#           es_select_recombine
# Produces a single child through selection and
# recombination of two parents from the population
# ---------------------------------------------------
# Inputs:
#   pop_chrom - individuals that form the population
#   pop_std   - standard deviations of the individuals
#   popSize   - number of individuals in the population
#   numVar    - number of dimensions of an individual
#   cType     - type of recombination desired
# Outputs:
#   child_chrom - resulting offspring
#   child_std   - std of the resulting offspring
# ---------------------------------------------------
# file: select_recombine.py
# ---------------------------------------------------
import numpy as np
# ---------------------------------------------------
def es_select_recombine(pop_chrom, pop_std, popsize,
                        numVar, cType):
    child_chrom = np.zeros(numVar)
    child_std = np.zeros(numVar)

    p = np.zeros(2, dtype = int)
    if cType == 1:
        # Randomly select two parents from the entire population
        p[0] = np.random.randint(popsize)
        p[1] = np.random.randint(popsize)

        # "Discrete Sexual Crossover"
        # Each solution feature and standard
        # deviation in the child is randomly
        # selected from one of two parents
        for i in range(numVar):
            ind_p1 = np.random.randint(1)
            ind_p2 = np.random.randint(1)
            child_chrom[i] = pop_chrom[p[ind_p1]][i]
            child_std[i] = pop_std[p[ind_p2]][i]

    elif cType == 2:
        # Randomly select two parents from
        # the entire population
        p[0] = np.random.randint(popsize)
        p[1] = np.random.randint(popsize)

        # Intermediate Sexual Crossover
        # Each solution feature and
        # standard deviation is the mean
        # of the corresponding feature/standard
        # deviation of the two parents
        for i in range(numVar):
            child_chrom[i] = np.mean([pop_chrom[p[0]][i],
                                      pop_chrom[p[1]][i]])
            child_std[i] = np.mean([pop_std[p[0]][i],
                                    pop_std[p[1]][i]])

    elif cType == 3:
        # Discrete Global Crossover
        # Each solution feature and standard
        # deviation in the child is randomly
        # selected from the entire population
        for i in range(numVar):
            # Randomly select two parents from t
            # he entire population
            p[0] = np.random.randint(popsize)
            p[1] = np.random.randint(popsize)

            # Produce one child by randomly picking
            # genes and std from one
            # of the selected parents
            child_chrom[i] = \
                pop_chrom[p[np.random.randint(1)]][i]
            child_std[i] = \
                pop_std[p[np.random.randint(1)]][i]

    elif cType == 4:
        # Intermediate Global Crossover
        # Each solution feature and standard
        # deviation in the child is the mean
        # of the corresponding feature
        # and standard deviation of parents
        # that are randomly selected
        # from the entire population
        for i in range(numVar):
            # Randomly select two parents from the entire population
            p[0] = np.random.randint(popsize)
            p[1] = np.random.randint(popsize)
            # Produce child by averaging the i-th gene from both parents
            child_chrom[i] = np.mean([pop_chrom[p[0]][i],
                                      pop_chrom[p[1]][i]])
            child_std[i] = np.mean([pop_std[p[0]][i],
                                    pop_std[p[1]][i]])

    else:
        print('crossover type not implemented')
        exit()

    return child_chrom, child_std






