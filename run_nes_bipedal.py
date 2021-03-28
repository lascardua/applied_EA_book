# ------------------------------------------------------------
#          Optimization for the Bipedal Walker
# ------------------------------------------------------------
# file: run_nes_bipedal.py
# ------------------------------------------------------------
import os
import numpy as np
from case_study_bipedal.nes import nes
import matplotlib.pyplot as plt
from case_study_bipedal.config import *
from case_study_bipedal.fitness_openai import fitness
# ------------------------------------------------------------
# Create folder to store training files
if not os.path.exists(training_folder):
    os.makedirs(training_folder)
# Set NES hyperparameters
f           = fitness
pop_size    = 100
sigma       = 0.1
max_iters   = 6000
if __name__ == '__main__':
    # perform optimization
    w, scores = nes(f,
                    pop_size,
                    sigma,
                    max_iters)
    # save the solution
    try:
        np.save(weights_file, w)
    except:
        print("save_weights -> error trying to save %s "
              % (weights_file))
        exit()
    # save the scores vector
    try:
        np.save(rewards_file, scores)
    except:
        print("save_weights -> error trying to save %s "
              % (rewards_file))
        exit()
    # plot the scores per iteration
    str = env_name
    plt.plot(scores)
    plt.title(str)
    plt.ylabel('mean population score')
    plt.xlabel('iteration')
    plt.show()





        


