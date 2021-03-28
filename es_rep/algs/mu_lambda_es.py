
import numpy as np
from auxiliary.init_rv import init_rv
from es_rep.utils.select_recombine import es_select_recombine, es_adjust_to_range


def mu_lambda_es(loss, theta, maxIterations, lb, ub, popsize, lambd):
    ## Settings
    numVar  = np.shape(theta)[0]   # problem dimension
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
            pop_chrom[popindex] = theta
        else:
            pop_chrom[popindex] = init_rv(1, numVar, lb, ub)
        # Standard deviation of the individual
        pop_std[popindex] = np.random.rand(numVar)
       # Cost
        pop_cost[popindex] = loss(pop_chrom[popindex])

    ## Children
    child_chrom = np.zeros((lambd,numVar))
    child_cost = np.zeros(lambd)
    child_std = np.zeros((lambd,numVar))

    ## Optimization
    # Constants for self - adaptation
    tau = 1 / np.sqrt(2 * np.sqrt(numVar)) # factor for adaptive mutation
    tauprime = 1 / np.sqrt(2 * numVar) # factor for adaptive mutation

    # Begin the optimization loop
    for id_iter in range(maxIterations):
        # Produce the children
        for childIndex in range(lambd):
            # Generate child
            child_chrom[childIndex], child_std[childIndex]  = es_select_recombine(pop_chrom, pop_std, popsize, numVar, crossoverType)

            # Adaptation
            rho_0 = np.random.randn(1)
            rho = np.random.randn(numVar)
            child_std[childIndex] = np.multiply(child_std[childIndex], np.exp(tauprime * rho_0 + tau * rho))

            # Perform mutation on the child
            r = np.random.randn(numVar)
            child_chrom[childIndex] = child_chrom[childIndex] + np.multiply(child_std[childIndex],r)

            # Keep Children within the search region
            child_chrom[childIndex] = es_adjust_to_range(child_chrom[childIndex], minDomain, maxDomain);

            # Calculate the cost of the child
            child_cost[childIndex] = loss(child_chrom[childIndex])


        # Only the children form the new population
        totalPop_chrom = child_chrom
        totalPop_cost = child_cost
        totalPop_std = child_std

        # Adjust the size of the population parameter
        popsize = lambd

        # Sort the population members from best (lower cost) to worst(higher cost)
        inds = np.argsort(totalPop_cost)
        totalPop_chrom = totalPop_chrom[inds]
        totalPop_cost  = totalPop_cost[inds]
        totalPop_std   = totalPop_std[inds]

        # Select the popSize best individuals
        pop_chrom = totalPop_chrom[0:popsize]
        pop_cost  = totalPop_cost[0:popsize]
        pop_std   = totalPop_std[0:popsize]

        # Store minimum and average costs
        if id_iter == 0:
            MinCost = np.array([pop_cost[0]])
            AvgCost = np.array([np.mean(pop_cost)])
            BestSol = np.array([pop_chrom[0]])
        else:
            MinCost = np.vstack((MinCost,pop_cost[0]))
            AvgCost = np.vstack((AvgCost, np.mean(pop_cost)))
            BestSol = np.vstack((BestSol,pop_chrom[0]))
        # # Display progress
        # print('Gen %d : min cost =  %.4f: ave cost = %.4f'%(genIndex, MinCost[genIndex], AvgCost[genIndex]))


    ind_best_theta = np.argmin(MinCost)
    best_theta = BestSol[ind_best_theta]
    best_scores = MinCost
    return best_theta, best_scores







