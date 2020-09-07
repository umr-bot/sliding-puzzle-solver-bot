import numpy as np
from env import env
class a():

    def __init__(self, Q):
        self.Q      = Q
        self.env    = env()
        self.Q[:,self.env.states.index(self.env.final_state)] = 0
    # Function to choose the next action 
    def choose_action(self, state): 
        epsilon = 0.1
        if np.random.uniform(0, 1) < epsilon:
            # choose random action with proability epsilon
            action = np.random.randint(4)
        else:
            # choose greedy/max action with probability 1-epsilon
            action = np.argmax(self.Q[:,state])
        return action

    def SARSA(self):
        gamma = 0.9
        alpha = 0.3
        episode = 0
        cnt = 0
        timestep_reward = []
        while episode < 10000:
            total_reward = 0
            S = self.env.reset()
            if episode % 1000 == 0 : print(episode)
            A = self.choose_action(self.env.states.index(S))
            for step in range(100):
                S_, R, terminate = self.env.step(A)
                total_reward += R
                si = self.env.states.index(S)
                si_ = self.env.states.index(S_)
                A_ = self.choose_action(si_)
                if terminate:
                    self.Q[A,si] += alpha*(R - self.Q[A,si])
                else:
                    self.Q[A,si] += alpha*(R + (gamma*self.Q[A_,si_]) - self.Q[A,si])
                S, A = S_, A_
                if terminate:
                    timestep_reward.append(total_reward)
                    break
            episode += 1
        return timestep_reward
############## TESTING ###############
agent = a(np.zeros((4,24)))
r = agent.SARSA()
avg_r = sum(r)/len(r)
print(agent.Q.T)
