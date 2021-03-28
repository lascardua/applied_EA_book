# --------------------------------------------------------------
#                    Fetch MOP
# --------------------------------------------------------------
# Inputs
#   fname - name of the MOP
#   n_dim - dimensionality of the solution vectors
# Outputs
#   f_cost  - cost function
#   n_goals - number of optimization goals
#   lb      - lower bound for the candidate solutions
#   ub      - upper bound for the candidate solutions
#   true_PF - true Pareto front of function f_cost
# --------------------------------------------------------------
# file: fetch_mop_problem.py
# --------------------------------------------------------------
import numpy as np
from test_functions_rep.mo.zdt1 import zdt1
from test_functions_rep.mo.zdt2 import zdt2
from test_functions_rep.mo.zdt3 import zdt3
from test_functions_rep.mo.zdt4 import zdt4
from test_functions_rep.mo.zdt6 import zdt6
# from test_functions_rep.mo.dtlz1_2d import dtlz1_2d
# --------------------------------------------------------------
def fetch_mop_problem(fname, n_dim):
    if fname == "ZDT1":
        f_cost = zdt1
        n_goals = 2
        ubc = 1
        lbc = 0
        lb = lbc * np.ones(n_dim)   # Lower bound for the
                                    # search space
        ub = ubc * np.ones(n_dim)   # Upper bound for the
                                    # search space
        from auxiliary.read_ZDT1_PF import read_zdt1_pf
        true_PF = read_zdt1_pf()

    if fname == "ZDT2":
        f_cost = zdt2
        n_goals = 2
        ubc = 1
        lbc = 0
        lb = lbc * np.ones(n_dim)   # Lower bound for the
                                    # search space
        ub = ubc * np.ones(n_dim)   # Upper bound for the
                                    # search space
        from auxiliary.read_ZDT2_PF import read_zdt2_pf
        true_PF = read_zdt2_pf()

    if fname == "ZDT3":
        f_cost = zdt3
        n_goals = 2
        ubc = 1
        lbc = 0
        lb = lbc * np.ones(n_dim)   # Lower bound for the
                                    # search space
        ub = ubc * np.ones(n_dim)   # Upper bound for the
                                    # search space
        from auxiliary.read_ZDT3_PF import read_zdt3_pf
        true_PF = read_zdt3_pf()

    if fname == "ZDT4":
        f_cost = zdt4
        n_goals = 2
        lb = np.zeros(n_dim)    # Lower bound for the
                                # search space
        ub = np.zeros(n_dim)    # Upper bound for the
                                # search space
        for ii in range(n_dim):
            if ii == 0:
                ub[ii] = 1
                lb[ii] = 0
            else:
                ub[ii] = 5
                lb[ii] = -5
        from auxiliary.read_ZDT4_PF import read_zdt4_pf
        true_PF = read_zdt4_pf()


    if fname == "ZDT6":
        f_cost = zdt6
        n_goals = 2
        ubc = 1
        lbc = 0
        lb = lbc * np.ones(n_dim)   # Lower bound for the
                                    # search space
        ub = ubc * np.ones(n_dim)   # Upper bound for the
                                    # search space
        from auxiliary.read_ZDT6_PF import read_zdt6_pf
        true_PF = read_zdt6_pf()

    # if fname == "DTLZ1_2d":
    #     f_cost = dtlz1_2d
    #     n_goals = 2
    #     ubc = 1
    #     lbc = 0
    #     lb = lbc * np.ones(n_dim)   # Lower bound for the
    #                                 # search space
    #     ub = ubc * np.ones(n_dim)   # Upper bound for the
    #                                 # search space
    #     from auxiliary.read_DTZ1_2d_PF import read_dtlz1_2d_pf
    #     true_PF = read_dtlz1_2d_pf()

    return f_cost,  n_goals, lb, ub, true_PF