
import numpy as np
from auxiliary.init_rv import init_rv
from es_rep.utils.adjust_to_range import es_adjust_to_range
from es_rep.utils.select_recombine import es_select_recombine

def mu_plus_one_es(loss, theta, maxIterations, lb, ub, popsize):
    ## Settings
    numVar = np.shape(theta)[0]  # problem dimension
    minDomain = lb
    maxDomain = ub

    crossoverType = 2   # 1 - Produce one child via "discrete sexual crossover"
                        # 2 - Produce one child via "intermediate sexual crossover"
                        # 3 - Produce one child via "discrete global crossover"
                        # 4 - Produce one child via "intermediate global crossover"

    ## Population
    pop_chrom = np.zeros((popsize,numVar))
    pop_cost = np.zeros(popsize)
    pop_std = np.zeros((popsize,numVar))


    for popindex in range(popsize):
        # generate individual
        if popindex == 0:
            # the initial solution is part of the first population
            pop_chrom[0] = theta
        else:
            pop_chrom[popindex] = init_rv(1, numVar, lb, ub)
        # Standard deviation of the individual
        pop_std[popindex] = np.random.rand(numVar)
       # Cost
        pop_cost[popindex] = loss(pop_chrom[popindex])


    ## Optimization
    for id_iter in range(maxIterations):
        # Generate child
        child_chrom, child_std  = es_select_recombine(pop_chrom, pop_std, popsize, numVar, crossoverType)

        # Perform mutation on the child
        child_chrom = child_chrom + np.multiply(child_std,np.random.randn(numVar))
        # Keep Children within the search region
        child_chrom = es_adjust_to_range(child_chrom, minDomain, maxDomain)
        # Calculate the cost of the child
        child_cost = loss(child_chrom)

        # Add the child to the population
        totalPop_chrom = np.vstack((pop_chrom, np.reshape(child_chrom, (1, numVar))))
        totalPop_cost = np.hstack((pop_cost, child_cost))
        totalPop_std = np.vstack((pop_std, child_std))

        # Sort the population members from best (lower cost) to worst(higher cost)
        inds = np.argsort(totalPop_cost)
        totalPop_chrom = totalPop_chrom[inds]
        totalPop_cost  = totalPop_cost[inds]
        totalPop_std   = totalPop_std[inds]

        # Remove the worst individual from the population
        pop_chrom = totalPop_chrom[0: popsize]
        pop_cost = totalPop_cost[0: popsize]
        pop_std = totalPop_std[0: popsize]

        # Store minimum cost and best solution
        if id_iter == 0:
            minCost = np.array([pop_cost[0]])
            bestSol = np.array([pop_chrom[0]])
        else:
            minCost = np.vstack((minCost,pop_cost[0]))
            bestSol = np.vstack((bestSol,pop_chrom[0]))

    ind_best = np.argmin(minCost)
    best_theta = bestSol[ind_best]
    best_scores = minCost
    return best_theta, best_scores






