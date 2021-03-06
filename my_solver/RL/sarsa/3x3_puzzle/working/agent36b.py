import numpy as np
from env36b import Env3
import matplotlib.pyplot as plt
import time

class Agent3():

    def __init__(self, Q):
        self.Q      = Q
        self.env    = Env3()
        final_state_index = self.env.states.index(self.env.final_state)
        self.Q[:,final_state_index] = 0
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
            #print("epsiode",episode)
            for step in range(num_steps):
                S_, R, terminate = self.env.step(S,A)
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
        #print(timestep_reward)
        return timestep_reward
    
    def solve(self, state):
        S = state.copy()
        done = False
        total_reward = 0
        cnt = 0
        states = []
        for cnt in range(100):
            time.sleep(0.1)
            A = np.argmax(self.Q[:,self.env.get_group_index(S)])
            print(f"Chose action {self.actions[A]} for state {S}")
            print(cnt)
            S_, reward, done = self.env.step(S, A,m=3,n=3)
            states.append(S_)
            S = S_
            total_reward += reward
            if done:
                print("state:",S)
                print(f"Episode reward: {total_reward}")
                time.sleep(1)
                return S,states

    # Uses full state set to solve puzzle using already trained SARSA Q set
    def test_agent_all_states(self):
        for test in range(5):
            print(f"Test #{test}")
            S = self.env.random_group_state()
            done = False
            total_reward = 0
            cnt = 0
            for cnt in range(100):
                time.sleep(0.1)
                A = np.argmax(self.Q[:,self.env.get_group_index(S)])
                print(f"Chose action {self.actions[A]} for state {S}")
                print(cnt)
                S_, reward, done = self.env.step(S, A,m=3,n=3)
                S = S_
                total_reward += reward
                if done:
                    print("state:",S)
                    print(f"Episode reward: {total_reward}")
                    time.sleep(1)
                    break

    def test_agent(self, n_tests=5, delay=0.1):
        states = self.env.gen_states()
        for test in range(n_tests):
            print(f"Test #{test}")
            S = self.env.reset()
            done = False
            total_reward = 0
            cnt = 0
            for cnt in range(100):
                time.sleep(delay)
                #self.env.render()
                A = np.argmax(self.Q[:,states.index(S)])
                if 0 == 0 : 
                    print(f"Chose action {self.actions[A]} for state {S}")
                    print(cnt)
                S_, reward, done = self.env.step(S, A)
                #print(done)
                S = S_
                total_reward += reward
                if done:
                    print("state:",S)
                    print(f"Episode reward: {total_reward}")
                    time.sleep(1)
                    break

def plot_rewards():
    alpha   = 0.1
    gamma   = 0.99
    eps     = [0.3]
    ##########
    avg_reward = []
    num_runs = 10
    for i in range(len(eps)):
        print("eps: "+str(eps[i])+" gamma: "+str(gamma)+ " aplha: "+str(alpha))
        run_reward = []
        for run in range(num_runs):
            print("run",run)
            agent3  = Agent3(np.zeros((4,120)))
            r_temp  = agent3.SARSA(epsilon=eps[i],alpha=alpha,gamma=gamma, num_episodes=5000,num_steps=10000)
            r_temp  = np.array( r_temp )
            run_reward.append(r_temp)
        tot = 0
        for i in range(1,len(run_reward)):
            shape = np.shape(run_reward[i])
            padded_array = np.zeros((10000))
            padded_array[:shape[0]] = run_reward[i]
            tot += padded_array
        tot = tot/(len(run_reward))
        avg_reward.append(tot)
    ################# Plotting average reward values
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
#agent_.test_agent()
# PYTHON TIMING FUNCTION
#timeit.timeit
def main():
    alpha   = 0.1
    gamma   = 0.99
    eps     = 0.3
    agent3  = Agent3(np.zeros((4,120)))
    agent3.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=5000,num_steps=10000)

