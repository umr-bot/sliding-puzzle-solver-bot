import numpy as np
class Env1():

    def __init__(self):
        self.final_state = ['0', 'x', 'x', '8', 'x', 'x', 'x', 'x', 'x']
        self.blank = '8'
        self.states = self.gen_states()
        self.grouped_states = self.grouped_3x3_states()

    def step(self, state_in, action):
        state = state_in.copy()
        done = False
        state = self.Move(state, action)
        reward = -1
        if state[0] == '0' and state[3] == self.blank:
            done = True
            reward = 1000
        return state, reward, done
 
    # Return random state with all values in a state 'x' besides '0' and '8'
    def reset(self):
        return self.states[np.random.randint(len(self.states))]
    
    def random_group_state(self):
        return self.grouped_states[np.random.randint(len(self.grouped_states))][np.random.randint(len(self.grouped_states[0]))]

    def gen_states(self):
        states0b = [] 
        for i in range(81): 
            states0b.append(['x','x','x','x','x','x','x','x','x']) 
        for i in range(9): 
            for j in range(9): 
                if i!=j: 
                    states0b[9*i+j][j] = self.blank
                    states0b[(9*i)+j][i] = '0' 
        for i in range(9): 
            states0b.remove(['x','x','x','x','x','x','x','x','x']) 
        return states0b
   
    def get_group_index(self, state):
       for i in range(len(self.states)):
           if state in self.grouped_states[i]: 
               return i

    def grouped_3x3_states(self):
        with open('solvable_states.txt','r') as file: 
            states = file.readline()
        states = [x.strip(" '") for x in states.split(',')] 
        grouped_states = [ [] for i in range(81)] 
        for state in states: 
            index = state.index('0')*9 + state.index('8') 
            grouped_states[index].append(state) 
        grouped_states = list(filter([].__ne__, grouped_states)) 
        return [[list(y) for y in x] for x in grouped_states]

    # puzzle with m rows and n columns
    def Move(self,state_in, move,m=3,n=3):
        state = state_in.copy()
        up,down,left,right = 0,1,2,3
        B_index     = state.index(self.blank)
        if move == up:
            if B_index >= n:
                state[B_index] = state[B_index-n]
                state[B_index-n] = self.blank
        if move == down:
            if B_index < (m*n) - n:
                state[B_index] = state[B_index+n]
                state[B_index+n] = self.blank
        if move == left:
            if B_index%n != 0:
                state[B_index] = state[B_index-1]
                state[B_index-1] = self.blank
        if move == right:
            if B_index%n != n-1:
                state[B_index] = state[B_index+1]
                state[B_index+1] = self.blank
        return state

#########TESTING############
#e = Env1()
#up,down,left,right = 0,1,2,3
#states = e.gen_states()
#state = states[71]
#print("Original state",state)
#print("Moved state",e.Move(state,right))
