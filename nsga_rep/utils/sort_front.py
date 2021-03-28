import numpy as np
from nsga_rep.utils.crowded_comparison import crowded_comparison_operator
# ----------------------------------------------------------------
def sort_front(pop_chrom, pop_fit, pop_rank, pop_cdist,front):
    # indices dos elementos que estao no front
    inds_front = front[:]
    # nc - contador de vitorias na comparacao cco
    nc = np.zeros(len(inds_front), dtype=int)
    for i in range(len(inds_front)):
        for j in range(len(inds_front)):
            if i == j:
                continue
            cco = crowded_comparison_operator(pop_rank[inds_front[i]], pop_cdist[inds_front[i]], pop_rank[inds_front[j]], pop_cdist[inds_front[j]])
            if cco == 0:
                nc[i] = nc[i] + 1
            else:
                nc[j] = nc[j] + 1
    # ordena as solucoes em ordem decrescente de vitorias no indice cco
    inds_nc = np.argsort(-nc)
    inds_cco = np.zeros(len(inds_nc),dtype=int)
    for i in range(len(inds_nc)):
        inds_cco[i] = inds_front[inds_nc[i]]

    sols_front_chrom = pop_chrom[inds_cco]
    sols_front_fit = pop_fit[inds_cco]
    sols_front_rank = pop_rank[inds_cco]
    sols_front_cdist = pop_cdist[inds_cco]

    return sols_front_chrom, sols_front_fit, sols_front_rank, sols_front_cdist