import numpy as np
def init_rv(M, N, lb, ub):
    # -------------------------------------------------
    # Initiates a real-valued population of M individuals
    # and N decision variables in the interval [lb,ub]
    # -------------------------------------------------
    pop_chrom = np.random.uniform(lb, ub, (M, N))
    pop_chrom[0] = lb
    pop_chrom[-1] = ub
    return pop_chrom
