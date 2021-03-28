import numpy as np
def init_bin(M,N,nbits):
    # -------------------------------------------------
    # Initiates a binary/gray coded population of
    # M individuals with nbits bits
    # -------------------------------------------------
    pop_chrom = np.random.randint(0,2,size=(M,nbits))
    return pop_chrom

