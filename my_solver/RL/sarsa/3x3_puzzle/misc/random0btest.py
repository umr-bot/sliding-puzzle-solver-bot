import numpy as np
from env import env
class Agent1():

    def __init__(self):
        self.e = env()
Q = np.zeros((4,181440))
Q[:,3] = 0
agent1 = Agent1()
alpha  = 0.1
gamma  = 0.9
epsilon= 0.15
num_episodes = 100
solved_steps_list = []
si = 0
for episode in range(num_episodes):
    steps = 0
    S = agent1.e.reset()
    total_reward = 0
    A       = np.random.randint(4)
    print(Q[A,si])
    print("episode",episode)
    terminate = False
    while True:
        if steps%100 == 0: print("step",steps)
        steps        += 1
        S_            = agent1.e.transpose(A)
        R             = -1
        total_reward += R
        if agent1.e.state[0] == '0': terminate = True
        #A_            = np.random.randint(4)
        si = agent1.e.solvable_states.index(S)
        si_= agent1.e.solvable_states.index(S_)
        if np.random.uniform(0, 1) < epsilon:
            A_ = np.random.randint(4)
        else:
            A_ = np.argmax(Q[:,si])
        if terminate:
            Q[A,si] += alpha*(R - Q[A,si])
            print(Q[A,si])
        else:
            Q[A,si] += alpha*(R + (gamma*Q[A_,si_]) - Q[A,si])
        S, A = S_, A_
        total_reward += R
        if terminate:
#            print("solved in " + str(steps) + " steps")
#            print("final state", agent1.e.state)
            solved_steps_list.append(steps)
            break
    solved_steps_list.append(steps)

avg_num_steps = sum(solved_steps_list)/len(solved_steps_list)
print("Average nummber of steps",avg_num_steps)
