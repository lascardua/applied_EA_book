import numpy as np
def init_int(M,N,lb, ub):
    # -------------------------------------------------
    # Initiates an integer coded population of
    # M individuals
    # -------------------------------------------------
    pop_chrom = np.random.randint(lb,ub,size=(M,N))
    return pop_chrom

