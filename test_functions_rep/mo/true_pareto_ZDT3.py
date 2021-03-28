
# https://github.com/jMetal/jMetalPy/blob/master/resources/reference_front/ZDT3.pf
import numpy as np


def read_zdt3():
    f= open("zdt3.txt", mode='r')
    temp = np.zeros(2)
    lines = f.readlines()
    xlist = []
    for line in lines:
        line = line.rstrip().split('\t')
        temp[0] = float(line[0])
        temp[1] = float(line[1])
        xlist.append([temp[0], temp[1]])
    f.close()
    xarray = np.array(xlist)
    return xarray

zdt_pf = read_zdt3()

import matplotlib.pyplot as plt
plt.xlabel('$f_1$', fontsize=15)
plt.ylabel('$f_2$', fontsize=15)
plt.scatter(zdt_pf[:,0],zdt_pf[:,1])
plt.title('ZDT3')
plt.show()

# n_samples = 99
# n_dim = 2
# n_goals = 2
#
# a = 0
# b = 1
# x1 = np.linspace(0,1,n_samples)
# # a condicao de que g(x) = 1 no front de Pareto faz com que
# # x2 seja obrigatoriamente zero no caso de n_goals = 2
# x2 = np.zeros(n_samples)
#
# # ZDT3
# pareto_front = np.zeros((n_samples, n_goals))
# pareto_set = np.zeros((n_samples, n_dim))
# for id in range(n_samples):
#     f1 = x1[id]
#     f2 = 1 - np.sqrt(x1[id]) - x1[id]*np.sin(10*np.pi*x1[id]) # como g = 1 no front, a equacao se reduz a isso
#     if id == 0:
#         pareto_front = np.array([f1, f2])
#         pareto_set = np.array([x1[id], x2[id]])
#     else:
#         pareto_front = np.vstack((pareto_front,np.array([f1, f2])))
#         pareto_set = np.vstack((pareto_set,np.array([x1[id], x2[id]])))
#
#
# import matplotlib.pyplot as plt
# plt.xlabel('$f_1$', fontsize=15)
# plt.ylabel('$f_2$', fontsize=15)
# plt.scatter(pareto_front[:,0],pareto_front[:,1])
# plt.title('ZDT3')
# plt.show()


