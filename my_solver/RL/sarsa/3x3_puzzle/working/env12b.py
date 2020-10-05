import numpy as np
import itertools
from collections import defaultdict

class Env2():
    def __init__(self):
        self.final_state = ['1', '2', '8', 'x', 'x', 'x'] # not used but here for explicity
        self.blank       = '8'
        self.states = self.gen_states()
        self.grouped_states = self.grouped_3x3_states()

    def step(self, state_in, action):
        state = state_in.copy()
        done = False
        state = self.Move(state, action)
        reward = -1
        if state[0] == '1' and state[1] == '2' and state[2] == self.blank:
            done = True
            reward = 1000
        return state, reward, done
    # Return random state with all values in a state 'x' besides '0' and '8'
    def reset(self):
        return self.states[np.random.randint(len(self.states))]
    
    def convert_3x2_to_3x3(self,index):
        if index >= 4:               return index + 3
        if index >= 2 and index < 4: return index + 2
        if index < 2:                return index + 1

    def get_group_index(self):
        for i in range(6):
            for j in range(6):
                 for k in range(6):
                     if i!=j and i!=k and j!=k:
                         if S in e.grouped_states[(i,j,k)]: 
                             print("(i,j,k)",i,j,k)
                             return (i,j,k)
    def grouped_3x3_states(self):
        with open('solvable_states.txt','r') as file:
            states = file.readline()
        states = [x.strip(" '") for x in states.split(',')]
        grouped_states = defaultdict(list)
        for state in states:
            if (state.index('1') != state.index('2')) and (state.index('1') != state.index('8')) and (state.index('2') != state.index('8')):
                if (state.index('1') %3 != 0) and (state.index('2') %3 != 0) and (state.index('8') %3 != 0):
                    grouped_states[(state.index('1'),state.index('2'), state.index('8'))].append(list(state))
        return grouped_states

    def gen_states(self):
        state_tuples = set(itertools.permutations('12Bxxx', 6))
        states = [list(state_tuple) for state_tuple in state_tuples]
        states.sort()
        return states
    # puzzle with m rows and n columns
    def Move(self,state_in, move,m=3,n=2):
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

