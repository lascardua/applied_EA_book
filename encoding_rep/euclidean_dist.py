import numpy as np
def euclidean_dist(x,y):
    dist = np.sqrt(np.sum((x - y) ** 2));
    return dist