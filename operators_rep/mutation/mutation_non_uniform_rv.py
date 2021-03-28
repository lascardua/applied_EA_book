# -------------------------------------------------------------
#                 Non-Uniform Mutation
#   VER ITEM 5.3.2 NON-UNIFORM MUTATION DE
# Michalewicz - GeneticAlgorithms+DataStructures=EvolutionPrograms
# -------------------------------------------------------------
# Inputs:
#   x  - n-dimensional individual to be mutated
#   pm - probability that a gene will undergo mutation
#   a  - lower bound for the values of the genes
#   b  - upper bound for the values of the genes
# Output:
#   mutated_x - mutated individual
# -------------------------------------------------------------
# file: mutation_non_uniform_rv.py
# -------------------------------------------------------------
import numpy as np
# -------------------------------------------------------------
def mutation_non_uniform_rv(x, pm, xL, xU,t,tmax,b):
    num_genes = np.size(x)
    # create the mutated individual
    mutated_x = np.copy(x)
    # Uniform mutation
    for k in range(num_genes):
        # Generate a random number
        r = np.random.uniform()
        tau = -1
        if r < 0.5:
            tau = 1
        # Mutate this gene?
        if r < pm:
            mutated_x[k] = x[k] + tau*(xU[k] - xL[k])*(1-r**((1-(t/tmax)**b)))
    # Return the mutated chromosome
    return mutated_x

x = np.array([3])
pm = 1
xL = np.array([1])
xU = np.array([8])
t = 250
tmax = 300
b = 5
c = mutation_non_uniform_rv(x, pm, xL, xU,t,tmax,b)

print(c)