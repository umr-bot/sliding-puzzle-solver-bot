import numpy as np
from env_2x2 import env_2x2
import matplotlib.pyplot as plt
import time

class Agent_2x2():

    def __init__(self, Q):
        self.Q      = Q
        self.env    = env_2x2()
        self.Q[:,self.env.states.index(self.env.final_state)] = 0
        self.actions = ['up','down','left','right'] # 0,1,2,3

    # Function to choose the next action 
    def choose_action(self, state, epsilon=0.1):
        if np.random.uniform(0, 1) < epsilon:
            # choose random action with proability epsilon
            action = np.random.randint(4)
        else:
            # choose greedy/max action with probability 1-epsilon
            action = np.argmax(self.Q[:,state])
        return action

    def SARSA(self, gamma=0.9, alpha=0.1, epsilon=0.1, num_episodes=200, num_steps=100):
        timestep_reward = []
        for episode in range(num_episodes):
            total_reward = 0
            S = self.env.reset()
            A = self.choose_action(state=self.env.states.index(S), epsilon=epsilon)
            for step in range(num_steps):
                S_, R, terminate = self.env.step(A)
                total_reward += R
                si = self.env.states.index(S)   #index of state S in Q-table
                si_ = self.env.states.index(S_) #index of state S_ in Q-table
                A_ = self.choose_action(state=si_, epsilon=epsilon)
                if terminate:
                    self.Q[A,si] += alpha*(R - self.Q[A,si])
                else:
                    self.Q[A,si] += alpha*(R + (gamma*self.Q[A_,si_]) - self.Q[A,si])
                S, A = S_, A_
                if terminate:
                    timestep_reward.append(total_reward)
                    break
            timestep_reward.append(total_reward)
        
        return timestep_reward
    
    def solve(self, state, delay=0.1):
        total_reward = 0
        S = state
        self.env.state = S
        index = self.env.states.index(S)
        done = False
        states = []
        states.append(list(S))
        for cnt in range(100):
            time.sleep(delay)
            A = np.argmax(self.Q[:,self.env.states.index(S)])
            print(f"Chose action {self.actions[A]} for state {S}")
            print(cnt)
            S_, reward, done = self.env.step(A)
            print(S_)
            states.append(list(S_))
            S = S_
            total_reward += reward
            if done:
                print("state:",S)
                print(f"Episode reward: {total_reward}")
                time.sleep(1)
                return S,states

    def test_agent(self, n_tests=5, delay=0.1):
        for test in range(n_tests):
            print(f"Test #{test}")
            total_reward = 0
            s = self.env.reset()
            S = self.env.states.index(s)
            done = False
            for cnt in range(100):
                time.sleep(delay)
                A = np.argmax(self.Q[:,S])
                print(f"Chose action {self.actions[A]} for state {s}")
                print(cnt)
                s, reward, done = self.env.step(A)
                S_ = self.env.states.index(s)
                S = S_
                total_reward += reward
                if done:
                    print("state:",self.env.states[S])
                    print(f"Episode reward: {total_reward}")
                    time.sleep(1)
                    break

def plot_rewards():
    alpha   = 0.3
    gamma   = 0.9
    eps     = [0,0.015,0.15,0.3]
    ##########
    #r = dict() # random placeholder values in the list
    avg_reward = []
    num_runs = 100
    for i in range(len(eps)):
        print("eps: "+str(eps[i])+" gamma: "+str(gamma)+ " aplha: "+str(alpha))
        run_reward = []
        for run in range(num_runs):
            agent_  = Agent_2x2(np.zeros((4,24)))
            r_temp  = agent_.SARSA(epsilon=eps[i],alpha=alpha,gamma=gamma, num_episodes=100,num_steps=100)
            r_temp  = np.array( r_temp )
            run_reward.append(r_temp)
            print("run",run)
        tot = 0
        for i in range(1,len(run_reward)):
            shape = np.shape(run_reward[i])
            padded_array = np.zeros((200))
            padded_array[:shape[0]] = run_reward[i]
            tot += padded_array
        tot = tot/(len(run_reward))
        avg_reward.append(tot)
    ################## Plotting average reward values
    for i in range(len(eps)):
        lab = 'eps=' + str(eps[i])
        plt.plot(avg_reward[i],label=lab)
        #plt.plot(r_temp)
    plt.title("Number of runs="+str(num_runs))
    plt.xlabel("Number of episodes") 
    plt.ylabel("Average reward across all runs") 
    plt.legend(loc="lower right")
    plt.show()
################################################
####RUNNING learnt sarsa algorithm####
def main():
    alpha   = 0.3
    gamma   = 0.9
    eps     = 0.15
    agent_  = Agent_2x2(np.zeros((4,24)))
    agent_.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=100,num_steps=100)
    agent_.test_agent()
