import numpy as np
import itertools
class Env3():
    def __init__(self):
        self.final_state = ['3', 'x', 'x', '6', 'B', 'x'] # not used but here for explicity
        self.states = self.gen_states()
    def step(self, state_in, action):
        state = state_in.copy()
        done = False
        state = self.Move(state, action)
        reward = -1
        if state[0] == '3' and state[3] == '6' and state[4] == 'B':
            done = True
            reward = 1000
        return state, reward, done
    # Return random state with all values in a state 'x' besides '0' and 'B'
    def reset(self):
        return self.states[np.random.randint(len(self.states))]

    def gen_states(self):
        state_tuples = set(itertools.permutations('36Bxxx', 6))
        states = [list(state_tuple) for state_tuple in state_tuples]
        states.sort()
        return states
    # puzzle with m rows and n columns
    def Move(self,state_in, move,m=2,n=3):
        state = state_in.copy()
        up,down,left,right = 0,1,2,3
        B_index     = state.index('B')
        #one_index   = state.index('0')
        temp_state  = 'x'
        if move == up:
            if B_index >= n:
                state[B_index] = state[B_index-n]
                state[B_index-n] = 'B'
        if move == down:
            if B_index < (m*n) - n:
                state[B_index] = state[B_index+n]
                state[B_index+n] = 'B'
        if move == left:
            if B_index%n != 0:
                state[B_index] = state[B_index-1]
                state[B_index-1] = 'B'
        if move == right:
            if B_index%n != n-1:
                state[B_index] = state[B_index+1]
                state[B_index+1] = 'B'
        return state

