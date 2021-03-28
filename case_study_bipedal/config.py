#--------------------------------------------------------------
# Configuration File for the Bipedal Walker Problem
#--------------------------------------------------------------
# file: config.py
#--------------------------------------------------------------
from case_study_bipedal.mlp import ANN
#--------------------------------------------------------------
# Simulator
env_name = 'BipedalWalker-v3' # simulator name
n_fevals = 1                  # if n_fevals>1 then we are using
                              # resampling
#--------------------------------------------------------------
# Settings for the NN hidden layer
n_hidden = 32       # number of neurons
activ_f = 'tanh'    # activation function

# Get the initial weights and the dimensionality of the weights
# vector
model = ANN(env_name, n_hidden, activ_f)
nVar = model.n_params
initial_w = model.get_weights()
# delete this NN
del model
#--------------------------------------------------------------
# Select the optimizer for NES
# optimizer = 'SGD_momentum'
# optimizer = 'SGD'
optimizer = 'Adam'
#--------------------------------------------------------------
# Test episodes
n_reps_test     = 100   # number of test episodes
save_interval   = 500   # periodically save the NN weights
#--------------------------------------------------------------
# Folders and files
training_folder = "./box2d_training/" + env_name + "/nes/"+optimizer+"/"
weights_file    = training_folder + 'weights.npy'
rewards_file    = training_folder + 'rewards.npy'









