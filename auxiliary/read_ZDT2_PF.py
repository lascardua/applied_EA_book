import numpy as np
def read_zdt2_pf():
    filename = "../test_functions_rep/mo/ZDT2.txt"
    f= open(filename, mode='r')
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