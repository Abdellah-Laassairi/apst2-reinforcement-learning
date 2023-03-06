
import gymnasium as gym
import pygame
import sys
import argparse
from tools.qlearning import *
from tools.sarsa import *

def main(env, learning_method, save):
    """
    main function to launch reinforcement learning agent
    """

    if env == 'CartPole-v0':
        env = gym.make("CartPole-v0", render_mode="human")
        observation, info = env.reset(seed=42)
    elif env == 'frozen_lake':
        env = gym.make("FrozenLake-v1", render_mode="human")
        observation, info = env.reset(seed=42)

    if learning_method == 'QLearning':
        q_table = q_train_greedy(env, weights="data/q_table.npy")
        if save :
            np.save("data/q_table", q_table)

    elif learning_method == 'SARSA':
        sarsa_train(env)
    


            
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--method",
        dest="method",
        type=str,
        default="QLearning",
        help=
        "options : QLearning, SARSA"
    )
    parser.add_argument(
        "--env",
        dest="env",
        type=str,
        default="frozen_lake",
        help="options : frozen_lake, acrobot")
    
    parser.add_argument(
        "--save",
        dest="save",
        type=bool,
        default=True,
        help="Save the trained model or weights")
    args = parser.parse_args()


    main(args.env, args.method, args.save)