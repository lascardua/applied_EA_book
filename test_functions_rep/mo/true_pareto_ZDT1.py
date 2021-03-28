# https://github.com/jMetal/jMetalPy/blob/master/resources/reference_front/ZDT1.pf
import numpy as np

def read_zdt1():
    f= open("zdt1.txt", mode='r')
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

zdt_pf = read_zdt1()

# ------------------------------------------
# Generate PF
# ------------------------------------------
def generate_zdt1_pf():
    # define the number of points to be generated
    n_samples = 1000
    # by definition, we have f1 = x_1
    x1 = np.linspace(0, 1, n_samples)
    f1 = x1
    # at the front, we have g(x_2, ..., x_n) = 1,
    # thus f2 = 1 - np.sqrt(f1)
    f2 = 1 - np.sqrt(f1)
    pareto_front = np.array([f1, f2]).T
    return pareto_front
pareto_front = generate_zdt1_pf()
# --------------------------------------------
# Compare the results
# --------------------------------------------
import matplotlib.pyplot as plt
plt.xlabel('$f_1$', fontsize=15)
plt.ylabel('$f_2$', fontsize=15)
plt.plot(pareto_front[:,0],pareto_front[:,1], label = 'Computed PF')
plt.plot(zdt_pf[:,0],zdt_pf[:,1],'b+' , label = 'True PF')
plt.title('ZDT1')
plt.legend()
plt.show()


