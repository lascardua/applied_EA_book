from auxiliary.save_fig import save_fig
import numpy as np
def plot_boxplots(fig_file,data, xticklables, title, xlabel, ylabel):
    data_to_plot = data

    # Create a figure instance
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    bp = plt.boxplot(data_to_plot, notch=0, sym='+', vert=1, whis=1.5)
    ticks = np.arange(1,len(xticklables)+1)
    plt.xticks(ticks,labels=xticklables)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.yscale('log')
    plt.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
    plt.title(title)

    # change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='k', linewidth=2)

    # print the figure
    save_fig(fig_file)

