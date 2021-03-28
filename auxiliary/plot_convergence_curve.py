
# Plot the convergence curve
import matplotlib.pyplot as plt
import numpy as np
def plot_convergence_curve(fig_name,title_str,fbest_h,fig_size_x = 8,fig_size_y = 4, dpi=1000):
    num_vals = len(fbest_h)
    t = np.linspace(0, num_vals-1, num_vals)
    fig, ax = plt.subplots(figsize=(fig_size_x,fig_size_y), dpi=dpi) # figura 800x600 pixels
    ax.plot(t, fbest_h,c='0.35')
    #ax.set_xlabel(r'$\mathit{iteration}$', fontsize=18)
    #ax.set_ylabel(r'$f_o$', fontsize=18)
    ax.set_xlabel(r'$\mathit{iteration}$')
    ax.set_ylabel(r'$f_o$')
    ax.set_title(title_str)
    ax.grid(True)
    plt.savefig(fig_name,format="eps",dpi=dpi)

