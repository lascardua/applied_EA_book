import matplotlib.pyplot as plt
def save_fig(fname, display = True):
    dpi = 1000
    plt.savefig(fname, format="eps", dpi=dpi)
    if display:
        plt.show()