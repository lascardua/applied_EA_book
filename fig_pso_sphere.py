# --------------------------------------------------
#      PSO Algorithm Minimizing a Sphere
# --------------------------------------------------
# file: fig_pso_sphere.py
# --------------------------------------------------
# Import the necessary libraries and functions
import numpy as np
from pso_rep.pso import pso
import matplotlib.pyplot as plt
from fitnessf_max.fitnessf_sphere_rv import \
    fitness_sphere_rv
# --------------------------------------------------
# Plot the convergence curve
# --------------------------------------------------
def plot_convergence_curve(fig_name,title_str,fbest_h,
                           fig_size_x = 8,fig_size_y = 4,
                           dpi=1000):
    num_vals = len(fbest_h)
    t = np.linspace(0, num_vals-1, num_vals)
    fig, ax = plt.subplots(figsize=(fig_size_x,fig_size_y),
                           dpi=dpi) # figura 800x600 pixels
    ax.plot(t, fbest_h,c='0.35')
    #ax.set_xlabel(r'$\mathit{iteration}$', fontsize=18)
    #ax.set_ylabel(r'$f_o$', fontsize=18)
    ax.set_xlabel(r'$\mathit{iteration}$')
    ax.set_ylabel(r'$f_o$')
    ax.set_title(title_str)
    ax.grid(True)
    plt.savefig(fig_name,format="eps",dpi=dpi)
# --------------------------------------------------
# Minimization
# --------------------------------------------------
# 1 - Define the upper and lower bounds of the search space
ndim = 20               # Number of dimensions of the problem
lb = -5*np.ones(ndim)   # Bounds of the search space
ub = 5*np.ones(ndim)

# 2 - Define the parameters for the optimization
noP = 50        # Number of particles
maxIters = 300  # Number of optimization iterations

# 3 - Parameters for the PSO
c1 = np.ones(ndim)  # Cognitive scaling parameter
c2 = np.ones(ndim)  # Social scaling parameter
w_min = 0.4*np.ones(ndim) # Minimum inertia
w_max = 0.9*np.ones(ndim) # Maximum inertia

# 4 - Define the cost function
fcost = fitness_sphere_rv

# 5 - Run the PSO algorithm
np.random.seed(123)
xbest, fbest, fbest_h = pso(fcost,maxIters,lb,ub,noP,c1,c2,w_min,w_max)

# 6 - Print the results
print('xbest: {}'.format(xbest))
print('fbest: {}'.format(fbest))

# 7 - Plot the convergence curve--------------------------
from auxiliary.plot_convergence_curve \
    import plot_convergence_curve
fig_file= 'figure_4_2.eps'

title_str=\
"PSO Minimizing a " + str(ndim) + "-dimensional Sphere"
plot_convergence_curve(fig_file,title_str,fbest_h)


