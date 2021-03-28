# ------------------------------------------------------------
#                    MLP with one hidden layer
# ------------------------------------------------------------
# env_name      - name of the simulation environment
# n_hidden      - number of neurons in the hidden layer
# activ_f       - activation function
# ------------------------------------------------------------
# file: mlp.py
# ------------------------------------------------------------
import os
import gym
import numpy as np
# ------------------------------------------------------------
# ReLU
def relu(x):
    return x * (x > 0)
# Sigmoid
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
# tanh
def tanh(x):
    return np.tanh(x)
# ------------------------------------------------------------
class ANN:
    def __init__(self, env_name, n_hidden, activ_f = 'tanh'):
        # Create OpenAI environment to obtain the number of input
        # and output neurons
        env = gym.make(env_name)
        self.D = len(env.reset())   # D - number input neurons
        self.M = n_hidden           # M - number hidden neurons
        self.K = env.action_space.shape[0] # K - number output
                                           # neurons
        # Set the activation function
        if activ_f == 'tanh':
            self.activ_f = tanh
        elif activ_f == 'relu':
            self.activ_f = relu
        else:
            print('Activation %s not implemented' % (activ_f))
            exit()
        # Obtain the maximum value of the output variables
        # It is assumed that the maximum and minimum values
        # have the same absolute value
        self.action_max = env.action_space.high[0]
        self.n_params = self.D * self.M + self.M +  \
                        self.M * self.K + self.K
        del env # don`t need it anymore
        # Random initialization of the weights
        self.W1 = \
            np.random.randn(self.D, self.M) / np.sqrt(self.D)
        self.b1 = \
            np.zeros(self.M)
        self.W2 = \
            np.random.randn(self.M, self.K) / np.sqrt(self.M)
        self.b2 = \
            np.zeros(self.K)
    # Compute the forward pass
    def forward(self, X):
        Z = self.activ_f(X.dot(self.W1) + self.b1)
        return np.tanh(Z.dot(self.W2) + self.b2) * \
               self.action_max
    # Compute a control action
    def sample_action(self, x):
        X = np.atleast_2d(x)
        Y = self.forward(X)
        return Y[0]  # the first row
    # Returns the weights a single vector
    def get_weights(self):
        return np.concatenate([self.W1.flatten(),
                               self.b1, self.W2.flatten(),
                               self.b2])
    # Receives a weights vector and converts it into the NN
    # weights
    def set_weights(self, params):
        # params is a flat list
        # unflatten into individual weights
        self.W1 = \
            params[:self.D * self.M].reshape(self.D, self.M)
        self.b1 = \
            params[self.D * self.M:self.D * self.M + self.M]
        self.W2 = \
            params[self.D * self.M + self.M:self.D * self.M
            + self.M + self.M * self.K].reshape(self.M,
                                                self.K)
        self.b2 = \
            params[-self.K:]
    # Saves the NN weights as a single vector in a file
    def save_weights(self, foldername):
        arqname = foldername + '/weights.npy'
        # Creates the folder
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        w = self.get_weights()
        try:
            np.save(arqname,w)
        except:
            print("FAILED saving weights to %s " % (arqname))
            exit()
    # Load the NN weights from a file
    def load_weights(self, foldername):
        try:
            fname = foldername+'weights.npy'
            w0 = np.load(fname)
            self.set_weights(w0)
            return w0
        except:
            print("FAILED loading weights from " % (fname))
            exit()
