# -------------------------------------------------------------
#            Polynomial Mutation
# -------------------------------------------------------------
# Inputs:
#   x           - individual to be mutated
#   pm          - probability that a gene will undergo mutation
#   a           - lower bound for the search scape
#   b           - upper bound for the search scape
#   eta_m       - distribution index in [20,100]
# Outputs:
#   mutated_x   - mutated individual
# -------------------------------------------------------------
# file: mutation_polynomial_rv.py
# -------------------------------------------------------------
import numpy as np
def mutation_polynomial_rv(x, pm, a, b, eta_m = 20):
    # No mutation is performed
    if pm == 0:
        return x
    # Decide if mutation will occur
    # if r < pm  --> perform mutation
    # if r >= pm --> do not perform mutation
    r = np.random.uniform()
    if r < pm:
        # number of genes
        n_var =len(x)
        # create the mutated individual
        mutated_x = np.copy(x)
        # polynomial mutation
        for k in range(n_var):
            u = np.random.uniform()
            if u <= 0.5:
                sig_L = (2 * u) ** (1 / (1+eta_m)) - 1
                mutated_x[k] = mutated_x[k] + \
                               sig_L*(mutated_x[k] - a[k])
            else:
                sig_R = 1 - (2 * (1 - u)) **  (1 / (1 + eta_m))
                mutated_x[k] = mutated_x[k] + \
                               sig_R * (b[k] - mutated_x[k])
    else:
        # Do not perform mutation
        mutated_x = x
    # Return the mutated individual
    return mutated_x

