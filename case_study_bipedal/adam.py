# ------------------------------------------------------------
# Adam optimizer for maximization
# ------------------------------------------------------------
# t         - discrete time
# m_adam    - past mean estimate
# v_adam    - past variance estimate
# w         - weights vector (candidate solution)
# grad      - gradient of F(w)
# ------------------------------------------------------------
# file: adam.py
# ------------------------------------------------------------
import numpy as np
# ------------------------------------------------------------
def adam_gd(t, m_adam, v_adam, w, grad):
    beta_1 = 0.9
    beta_2 = 0.999
    epsilon = 1e-08
    lr = 0.01
    g = grad
    t = t + 1  # because t starts with zero
    m_adam = beta_1 * m_adam + (1 - beta_1) * g
    v_adam = beta_2 * v_adam + (1 - beta_2) * np.power(g, 2)
    m_hat = m_adam / (1 - np.power(beta_1, t))
    v_hat = v_adam / (1 - np.power(beta_2, t))
    w = w + lr * m_hat / (np.sqrt(v_hat) + epsilon)
    return w, m_adam,v_adam