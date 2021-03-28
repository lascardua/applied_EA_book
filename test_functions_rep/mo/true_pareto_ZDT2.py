
# https://github.com/jMetal/jMetalPy/blob/master/resources/reference_front/ZDT2.pf
import numpy as np


def read_zdt2():
    f= open("zdt2.txt", mode='r')
    temp = np.zeros(2)
    lines = f.readlines()
    xlist = []
    for line in lines:
        line = line.rstrip().split(' ')
        temp[0] = float(line[0])
        temp[1] = float(line[1])
        xlist.append([temp[0], temp[1]])
    f.close()
    xarray = np.array(xlist)
    return xarray

zdt_pf = read_zdt2()

import matplotlib.pyplot as plt
plt.xlabel('$f_1$', fontsize=15)
plt.ylabel('$f_2$', fontsize=15)
plt.scatter(zdt_pf[:,0],zdt_pf[:,1])
plt.title('ZDT2')
plt.show()




