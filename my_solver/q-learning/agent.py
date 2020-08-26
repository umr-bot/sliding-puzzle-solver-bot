import numpy as np
### Functions choose_action and update taken from https://www.geeksforgeeks.org/sarsa-reinforcement-learning/?ref=rp
class agent():

    def __init__():
       
    #Function to choose the next action 
    def choose_action(state): 
        action=0
        if np.random.uniform(0, 1) < epsilon: 
            #action = env.action_space.sample() 
            pass
        else: 
            #action = np.argmax(Q[state, :]) 
            pass
        return action 
      
    #Function to learn the Q-value 
    def update(state, state2, reward, action, action2): 
        predict = Q[state, action] 
        target = reward + gamma * Q[state2, action2] 
        Q[state, action] = Q[state, action] + alpha * (target - predict) 
