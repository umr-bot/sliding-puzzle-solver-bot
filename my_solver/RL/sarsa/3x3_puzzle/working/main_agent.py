import numpy as np
from agent0b import Agent1
from agent_0_to_12_b import Agent2a
from agent12b import Agent2b
alpha   = 0.1
gamma   = 0.99
eps     = 0.3

state = ['2', '6', '4', '5', '7', '0', '8', '1', '3']
states =[]
if state[0] != '0':
    agent1  = Agent1(np.zeros((4,72)))
    agent1.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=400,num_steps=10000)
    state, temp_states = agent1.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent1 is",state)
if state[3] == '1' or state[6] == '1' or state[3] == '2' or state[6] == '2' or state[3] == '8' or state[6] == '8': 
    agent2a  = Agent2a(np.zeros((4,120)))
    agent2a.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=400,num_steps=10000)
    state, temp_states = agent2a.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent2a is",state)
if state[1] != '1' and state[2] != '2':
    agent2b  = Agent2b(np.zeros((4,120)))
    agent2b.SARSA(epsilon=eps,alpha=alpha,gamma=gamma, num_episodes=400,num_steps=10000)
    state, temp_states = agent2.solve(state) # states contains intial, in between and final states
    states.append(temp_states)
print("current state after agent2b is",state)

