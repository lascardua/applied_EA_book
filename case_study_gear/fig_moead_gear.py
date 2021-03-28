# ------------------------------------------------------------
#          Test the Gear Train System

# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from moead_rep.utils.dominates import dominates
from auxiliary.calc_idg_metric import calc_IDG_metric
from case_study_gear.gear_true_PF import true_PF, true_PS
# ------------------------------------------------------------

# Define cost function
def f_Gear(x):
    f1 = (1 / 6.931 - (x[0] * x[1]) / (x[2] * x[3]))** 2
    f2 = np.max(x)
    f = np.array([f1, f2])
    return f


n_dim = 4
n_goals = 2
ubc = 60
lbc = 12
lb = lbc*np.ones(n_dim)   # lower bound for the search space
ub = ubc*np.ones(n_dim)   # upper bound for the search space



f_fit_file = 'moead_f_cost.npy'
f_chrom_file = 'moead_f_chrom.npy'


F_cost = np.load(f_fit_file)
F_chrom = np.load(f_chrom_file)

# -- METRICS
# calculate the IDG metric
idg = calc_IDG_metric(true_PF, F_cost)
print('IDG: {} '.format(idg))

# Check if any solution found is dominated by other solution found
dominated = np.zeros(len(F_cost))
for i in range(len(F_cost)):
    for j in range(len(F_cost)):
        if i == j:
            continue
        if dominates(F_cost[j],F_cost[i]):
            dominated[i] = 1
            break


# Check if any solution found is equal to the true PS and / or is dominated by the true PF
dominated = np.zeros(len(F_cost))
equal = np.zeros(len(F_cost))
for i in range(len(F_cost)):
    for j in range(len(true_PF)):
        if np.all(true_PS[j]==F_chrom[i]):
            equal[i] = 1
        if dominates(true_PF[j],F_cost[i]):
            dominated[i] = 1
            break

new_PF = list()
new_PS = list()
for i in range(len(F_cost)):
    if dominated[i]==0 and equal[i]==0:
        new_PF.append(F_cost[i])
        new_PS.append(F_chrom[i])
new_PF = np.array(new_PF) # solucoes que não estão em true_PS mas que geram valores que já estão em true_PF
new_PS = np.array(new_PS)

# plot the scores per iteration
str = "MOEA/D Solving the Multi-Objective Gear Train Problem"
plt.scatter(F_cost[:,0], F_cost[:,1], label='MOEA/D', marker='+', c='k'),
plt.scatter(true_PF[:,0], true_PF[:,1], label='true PF', marker='.', c='k')
# if len(new_PF)>0:
#     plt.scatter(new_PF[:,0], new_PF[:,1], label='new PF', marker='+', c='r'),
plt.title(str)
plt.ylabel('$f_{1}$')
plt.xlabel('$f_{0}$')
plt.legend()


# Save the plot to a file
from auxiliary.save_fig import save_fig
fig_name =  \
    '../../../text/chapters/part_iv/case_studies/figs/fig_moead_solves_mo_gear_train.eps'
save_fig(fig_name, display = False)

        


