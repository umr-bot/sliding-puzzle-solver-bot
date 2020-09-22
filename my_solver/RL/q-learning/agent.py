import numpy as np
from env import env
import matplotlib.pyplot as plt

class agent():

    def __init__(self, Q):
        self.Q      = Q
        self.env    = env()
        self.Q[:,self.env.states.index(self.env.final_state)] = 0
    # Function to choose the next action 
    def choose_action(self, state, epsilon=0.1):
        if np.random.uniform(0, 1) < epsilon:
            # choose random action with proability epsilon
            action = np.random.randint(4)
        else:
            # choose greedy/max action with probability 1-epsilon
            action = np.argmax(self.Q[:,state])
        return action

    def q_learn(self, gamma=0.9, alpha=0.3, epsilon=0.1):
        episode = 0
        cnt = 0
        timestep_reward = []
        while episode < 10000:
            total_reward = 0
            S = self.env.reset()
            if episode % 5000 == 0 : print(episode)
            A = self.choose_action(state=self.env.states.index(S), epsilon=epsilon)
            for step in range(100):
                S_, R, terminate = self.env.step(A)
                total_reward += R
                si = self.env.states.index(S)
                si_ = self.env.states.index(S_)
                A_ = np.argmax(self.Q[:, si_])
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
eps = [0,0.01,0.1]
r = dict() # random placeholder values in the lise
for i in range(len(eps)):
    agent_ = agent(np.zeros((4,24)))
    r[i] = agent_.q_learn(epsilon=eps[i])
    #print(agent.Q.T)
plt_data = dict()

for i in range(len(r)):
    r_plt = []
    for j in range(1,len(r[i])+1): 
        r_plt.append(sum(r[i][0:j])/j)
    plt_data[i] = r_plt
    lab = 'eps=' + str(eps[i])
    plt.plot(r_plt[i],label=lab)

#ax = plt.gca() # not really neccesary to save the axes since its only usde once
#ax.legend(('e0'+str(eps[0]),'e1='+str(eps[1]),'e2='+str(2)))
plt.legend(loc="lower right")
plt.show()
