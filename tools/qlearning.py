
import numpy as np
from tqdm import *


def q_train_greedy(env, alpha=0.9, gamma=0.95, max_epsilon=1, epsilon=0.01, max_n_steps=100, n_episodes=10, weights="data/q_table.npy"):
    """ Q–learning algorithm (epsilon-greedy)
    
    """
    num_actions = env.action_space.n
    num_states = env.observation_space.n
    try :
        print("Loading Q-table saved weights...")
        q_table = np.load(weights)

    except :
        print("Error loading Q-table saved weights")
        print("Initiating new Q-table...")
        q_table = np.zeros((num_states, num_actions))

    rewards = []

    epsilon = max_epsilon

    print("Starting Q-learning algorithm...")
    for _ in trange(n_episodes):
        s = env.reset()[0]
        total_reward = 0
        for i in range(max_n_steps):
            U = np.random.uniform(0, 1)
            if U < epsilon:
                a = env.action_space.sample() # selecting action a at random from A 
            else:
                a = np.argmax(q_table[s]) # Select action a given X following policy derived from q;
            
            s_new, r, done, _ , _= env.step(a)
            
            q_table[s, a] = (1-alpha)*q_table[s, a] + alpha*(r + gamma*np.max(q_table[s_new]))
            
            s, total_reward = s_new, total_reward+r

            # if X is a terminal state then go to next episode;
            if done: 
                rewards.append(total_reward) 
                break
    env.close()
    print("Finished Q-learning algorithm.")
    print("Average reward: {}".format(np.mean(rewards)))
    return q_table