# -----------------------------------------------------------
# Update the external population
# -----------------------------------------------------------
# y_chrom   - new child
# y_cost    - cost of the new child
# EP_x      - individuals in the external population
# EP_f      - multi-objective costs of individuals in the
#               external population
# -----------------------------------------------------------
# file: update_EP.py
# -----------------------------------------------------------
import numpy as np
from moead_rep.utils.dominates import dominates
# -----------------------------------------------------------
def update_EP(y_chrom, y_cost, EP_x, EP_f):
    # Find solutions in EP_f that are not dominated
    # by y_cost
    ids_to_keep = list()
    for id_ep in range(len(EP_f)):
        if not dominates(y_cost, EP_f[id_ep]):
            ids_to_keep.append(id_ep)
    # Remove from EP all solutions dominated by
    # y_cost
    EP_f = EP_f[ids_to_keep]
    EP_x = EP_x[ids_to_keep]

    # Check if y_cost is dominated by any solution
    # in EP_f
    y_cost_dominated = False
    for id_f in range(len(EP_f)):
        # check domination
        if dominates(EP_f[id_f], y_cost):
            y_cost_dominated = True
            break
    # add y_chrom/y_cost to EP if no solutions in EP_f
    # dominate y_cost
    if y_cost_dominated == False:
        EP_f = np.vstack((EP_f, y_cost))
        EP_x = np.vstack((EP_x, y_chrom))
    return EP_x, EP_f