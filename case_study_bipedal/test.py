import os
from case_study_bipedal.mlp import ANN
from case_study_bipedal.config import n_hidden, n_reps_test
from case_study_bipedal.fitness_openai import run_episode

import numpy as np
import gym

def test(w, tests_folder , env_name, movie = True):



    if not os.path.exists(tests_folder):
        os.makedirs(tests_folder)

     # gym
    env = gym.make(env_name)
    if movie == True:
        env = gym.wrappers.Monitor(env, tests_folder, force=True)

    # model
    model = ANN(env_name, n_hidden, 'tanh')
    model.set_weights(w)

    # testando
    testscores = []
    for _ in range(n_reps_test):
        score = run_episode(env, model)
        testscores.append(score)

    # Resultados
    print("Test results of %s for %d episodes ." % (env_name, n_reps_test))
    print("mean : %f" % (np.mean(testscores)))
    print("std  : %f" % (np.std(testscores)))

    from datetime import datetime
    ftest = tests_folder + '/' + 'test_scores.txt'
    fp = open(ftest, 'a')
    fp.write("\n\n --- Test results of %s for %d test episodes." % (env_name, n_reps_test))
    fp.write("\ntimestamp        : %s" % str(datetime.now()))
    # fp.write("\nnum_eps_steps    : %d"%args.num_eps_steps)
    # fp.write("\nid_run              : %d" % (id_iter))
    fp.write("\nmean : %f" % (np.mean(testscores)))
    fp.write("\nstd  : %f" % (np.std(testscores)))
    fp.close()

    # Plots
    import matplotlib.pyplot as plt
    arqname = tests_folder + '/' + 'test_scores.png'
    plt.title(env_name)
    plt.plot(testscores)
    plt.ylabel('test scores')
    plt.xlabel('iteration')
    plt.savefig(arqname)
    plt.close(arqname)
    plt.close()

    return testscores
