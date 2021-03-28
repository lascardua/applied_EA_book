import numpy as np
def read_dtlz1_2d_pf():
    filename = "../test_functions_rep/mo/dtlz1_2d.txt"
    f= open(filename, mode='r')
    temp = np.zeros(2)
    lines = f.readlines()
    xlist = []
    for line in lines:
        line = line.rstrip().split(' ')
        data = line[0].rstrip().split('\t')
        temp[0] = float(data[0])
        temp[1] = float(data[1])
        xlist.append([temp[0], temp[1]])
    f.close()
    xarray = np.array(xlist)
    return xarray