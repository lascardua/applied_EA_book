import numpy as np
# ReLU
def relu(x):
    return x * (x > 0)

# Sigmoid
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# tanh
def tanh(x):
    return np.tanh(x)