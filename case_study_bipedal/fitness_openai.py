# ------------------------------------------------------------
#  Fitness function and episode function for the Bipedal Problem
# ------------------------------------------------------------
# file: fitness_openai.py
# ------------------------------------------------------------
import gym
import numpy as np
from case_study_bipedal.config import *
# ------------------------------------------------------------
# run an episode
# ------------------------------------------------------------
# env           -  simulator instance
# controller    - NN controller
# ------------------------------------------------------------
def run_episode(env,model):
    # run one episode and return the total reward
    episode_reward = 0
    done = False
    state = env.reset()
    while not done:
        # get the action
        action = model.sample_action(state)
        # perform the action
        state, reward, done, _ = env.step(action)
        # update total reward
        episode_reward += reward
    return episode_reward
# ------------------------------------------------------------
#  fitness function
# ------------------------------------------------------------
# w  - weights vector (candidate solution)
# ------------------------------------------------------------
def fitness(w):
    # instantiate neural controller with weights w
    controller = ANN(env_name, n_hidden, 'tanh')
    controller.set_weights(w)
    episode_reward = np.zeros(n_fevals)
    # instantiate the simulator
    env = gym.make(env_name)
    # perform n_fevals episodes
    for id in range(n_fevals):
        episode_reward[id] = run_episode(env,controller)
    # return the fitness value of w
    return np.mean(episode_reward)

