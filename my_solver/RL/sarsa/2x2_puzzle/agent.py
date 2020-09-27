import numpy as np
from env import env
import matplotlib.pyplot as plt
import time

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

    def test_agent(self, n_tests=5, delay=0.1):
        actions = ['up','down','left','right'] # 0,1,2,3
        for test in range(n_tests):
            print(f"Test #{test}")
            s = self.env.reset()
            S = self.env.states.index(s)
            done = False
            epsilon = 0
            total_reward = 0
            cnt = 0
            S_old = '0000'
            a = -1
            while cnt < 1000:
                time.sleep(delay)
                self.env.render()
                a = np.argmax(self.Q[:,S])
                if cnt < 25: print(f"Chose action {actions[a]} for state {s}")
                s, reward, done = self.env.step(a)
                S = self.env.states.index(s)
                S_old = S
                total_reward += reward
                if done:
                    print("state:",S)
                    print(f"Episode reward: {total_reward}")
                    time.sleep(1)
                    break
                cnt += 1

############### TESTING ###############
def plot_smooth(data,lab):
    from scipy.interpolate import make_interp_spline, BSpline
    
    # 10*len(data) represents number of points to make between 0 and len(data)
    xnew = np.linspace(0, len(data), 10*len(data))
    
    spl = make_interp_spline(np.arange(len(data)), data, k=3)  # type:BSpline
    data_smooth = spl(xnew)
    
    plt.plot(xnew, data_smooth,label=lab)

#def plot_rewards():
alpha   = 0.3
gamma   = [1,0.9,0.7,0.5]
eps     = 0.15
##########
#r = dict() # random placeholder values in the list
avg_reward = []
num_runs = 100
for i in range(len(gamma)):
    print("gamma: "+str(gamma[i])+" eps: "+str(eps)+ " aplha: "+str(alpha))
    run_reward = []
    for run in range(num_runs):
        agent_  = agent(np.zeros((4,24)))
        r_temp  = agent_.SARSA(epsilon=eps,alpha=alpha,gamma=gamma[i], num_episodes=100,num_steps=100)
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
for i in range(len(gamma)):
    lab = 'gamma=' + str(gamma[i])
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
