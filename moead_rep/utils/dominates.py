# -----------------------------------------------------------
# Returns 1 if x dominates y, otherwise returns 0
# -----------------------------------------------------------
def dominates(x, y):
    if all(x <= y) and any(x < y):
        return 1
    else:
        return 0