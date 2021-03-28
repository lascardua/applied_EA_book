def sgd_gd(w, grad):
    alpha = 0.02
    w = w + alpha * grad
    return w