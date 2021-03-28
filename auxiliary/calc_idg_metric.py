import numpy as np
def calc_IDG_metric(true_pf, approx_PF):
    from scipy.spatial.distance import euclidean
    normZ = len(true_pf)
    normA = len(approx_PF)

    # IGD
    dist = np.zeros((normZ, normA))
    for idz in range(normZ):
        for ida in range(normA):
            dist[idz, ida] = euclidean(true_pf[idz], approx_PF[ida])
    idg = 0
    for idz in range(normZ):
        idg = idg + np.min(dist[idz])
    idg = (1 / normZ) * idg
    return idg