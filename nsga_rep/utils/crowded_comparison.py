# -----------------------------------------------------------
#                CCO for NSGA-II
# -----------------------------------------------------------
# p0_rank       - rank of the first candidate
# p0_cdist      - crowding distance of the first candidate
# p1_rank       - rank of the second candidate
# p1_cdist      - crowding distance of the econd candidate
# -----------------------------------------------------------
# file: crowded_comparison.py
# -----------------------------------------------------------
def crowded_comparison_operator(p0_rank,p0_cdist, p1_rank, p1_cdist):
    if p0_rank < p1_rank:
        return 0
    if p1_rank < p0_rank:
        return 1
    if (p0_rank == p1_rank) and (p0_cdist > p1_cdist):
        return 0
    if (p0_rank == p1_rank) and (p1_cdist > p0_cdist):
        return 1
    return 0