import numpy as np
def read_zdt4_pf():
    filename = "../test_functions_rep/mo/ZDT4.txt"
    f= open(filename, mode='r')
    temp = np.zeros(2)
    lines = f.readlines()
    xlist = []
    for line in lines:
        line = line.rstrip().split('\n')
        line = line[0].split('\t')
        temp[0] = float(line[0])
        temp[1] = float(line[1])
        xlist.append([temp[0], temp[1]])
    f.close()
    xarray = np.array(xlist)
    return xarray