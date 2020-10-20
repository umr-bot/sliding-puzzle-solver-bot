import numpy as np
from env0b import Env1
from agent0b import Agent1
from agent_0_to_12_b import Agent2a
from agent12b import Agent2b
from agent36b import Agent3
from agent_2x2 import Agent_2x2
from image_saver import save_fig

alpha   = 0.1
gamma   = 0.95
eps     = 0.15
num_episodes = 10000

e = Env1()
state = e.random_group_state()
print("INITIAL STATE",state)
#state = ['2', '6', '4', '5', '7', '0', '8', '1', '3']

states =[]
if state[0] != '0':
    agent1  = Agent1(np.zeros((4,72)))
    agent1.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=num_episodes,num_steps=10000)
    state, temp_states = agent1.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent1 is",state)

if state[1] != '1' and state[2] != '2':
    if state[3] == '1' or state[6] == '1' or state[3] == '2' or state[6] == '2' or state[3] == '8' or state[6] == '8': 
        if state[1] != '1' and state[2] != '1' and state[1] != '2' and state[2] != '2':
            agent2a  = Agent2a(np.zeros((4,504)), agent='a1')
        if state[1] == '1' or state[2] == '1':
            agent2a  = Agent2a(np.zeros((4,504)), agent='a2',val='2')
        if state[1] == '2' or state[2] == '2':
            agent2a  = Agent2a(np.zeros((4,504)), agent='a2',val='1')

        agent2a.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=num_episodes,num_steps=10000)
        state, temp_states = agent2a.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent2a is",state)

if state[1] != '1' and state[2] != '2':
    agent2b  = Agent2b(np.zeros((4,120)))
    agent2b.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=num_episodes,num_steps=10000)
    state, temp_states = agent2b.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent2b is",state)

if state[3] != '3' or state[6] != '6':
    agent3  = Agent3(np.zeros((4,120)))
    agent3.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=num_episodes,num_steps=10000)
    state, temp_states = agent3.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent3 is",state)

agent_2x2  = Agent_2x2(np.zeros((4,24)))
agent_2x2.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=100,num_steps=100)
temp_state =state[4]+state[5]+state[7] + state[8]
fs, s_2x2 = agent_2x2.solve(temp_state)
ll = []
for s_ in s_2x2:
    ll.append(list(state[0:4]+s_[0:2]+list(state[6])+s_[2:4]))
states.append(ll)
print()
ss = []
for state in states:
    ss.append(np.array(state).astype(int)+1)
cnt = 0
for i in range(len(ss)):
    for j in range(len(ss[i])):
        save_fig(state=ss[i][j],state_num=cnt)
        print("state",cnt)
        print(ss[i][j].reshape(3,3))
        cnt += 1

