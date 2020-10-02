import numpy as np
class Env1():

    def __init__(self):
        self.final_state = ['0', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x']
        self.states = self.gen_states()
    def step(self, state, action):
        done = False
        state = self.Move(state, action)
        reward = -1
        if state[0] == '0' and state[3] == 'B':
            done = True
            reward = -1
        return state, reward, done
    # Return random state with all values in a state 'x' besides '0' and 'B'
    def reset(self):
        return self.states[np.random.randint(len(self.states))]

    def gen_states(self):
        states0b = [] 
        for i in range(81): 
            states0b.append(['x','x','x','x','x','x','x','x','x']) 
        for i in range(9): 
            for j in range(9): 
                if i!=j: 
                    states0b[9*i+j][j] = 'B' 
                    states0b[(9*i)+j][i] = '0' 
        for i in range(9): 
            states0b.remove(['x','x','x','x','x','x','x','x','x']) 
        return states0b

    def Move(self,state, move,N=3):
        up,down,left,right = 0,1,2,3
        B_index     = state.index('B')
        #one_index   = state.index('0')
        temp_state  = 'x'
        if move == up:
            if B_index >= N:
                state[B_index] = state[B_index-N]
                state[B_index-N] = 'B'
        if move == down:
            if B_index < N**2 - N:
                state[B_index] = state[B_index+N]
                state[B_index+N] = 'B'
        if move == left:
            if B_index%N != 0:
                state[B_index] = state[B_index-1]
                state[B_index-1] = 'B'
        if move == right:
            if B_index%N != N-1:
                state[B_index] = state[B_index+1]
                state[B_index+1] = 'B'
        return state
#########TESTING############
#e = Env1()
#up,down,left,right = 0,1,2,3
#states = e.gen_states()
#state = states[71]
#print("Original state",state)
#print("Moved state",e.Move(state,right))
