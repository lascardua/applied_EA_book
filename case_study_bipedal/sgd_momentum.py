import numpy as np
def sgd_momentum_gd(v_sgd,w, grad):
    alpha = 0.01
    mu = 0.9 # momentum
    v_sgd = mu*v_sgd + alpha*grad
    w = w + v_sgd
    return w, v_sgd