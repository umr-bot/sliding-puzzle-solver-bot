import numpy as np
import itertools
from collections import defaultdict

class Env2_a1():
    def __init__(self):
        self.final_state = ['x', '1', '2', 'x', '8', 'x'] # not used but here for explicity
        self.blank = '8'
        self.states = self.gen_states()
        self.tuple_grouped_states = self.tuple_grouped_3x3_states()
        self.grouped_states = self.grouped_states()
        
    def step(self, state_in, action,m=2,n=3):
        state = state_in.copy()
        done = False
        state = self.Move(state, action,m=m,n=n)
        reward = -1
        if m == 2 and n == 3:
            if state[1] == '1' and state[4] == self.blank and state[5] == '2':
                done = True
                reward = 1000
        if m == 3 and n == 3:
            if state[4] == '1' and state[7] == self.blank and state[8] == '2':
                done = True
                reward = 1000
        return state, reward, done
    # Return random state with all values in a state 'x' besides '0' and '8'
    def reset(self):
        return self.states[np.random.randint(len(self.states))]
    
    def get_group_index(self, state):
        for i in range(len(self.grouped_states)):
            if state in self.grouped_states[i]:
                return i

    def random_group_state(self):
        return self.grouped_states[np.random.randint(len(self.grouped_states))][np.random.randint(len(self.grouped_states[0]))]

    def grouped_states(self):
        state_list = [None] * 120
        for es in self.states:
            for key,item in self.tuple_grouped_states.items(): # key = index ; item = state
                if key == (self.convert_3x2_to_3x3(es.index('1')), self.convert_3x2_to_3x3(es.index('2')),self.convert_3x2_to_3x3(es.index('8'))):
                    state_list[self.states.index(es)] = item
        return state_list

    def convert_3x2_to_3x3(self,index):
        return index + 3

    def tuple_grouped_3x3_states(self):
        with open('solvable_states.txt','r') as file:
            states = file.readline()
        states = [x.strip(" '") for x in states.split(',')]
        grouped_states = defaultdict(list)
        for state in states:
            if (state.index('1') != state.index('2')) and (state.index('1') != state.index('8')) and (state.index('2') != state.index('8')):
                if (state.index('1') >= 3) and (state.index('2') >= 3) and (state.index('8') >= 3):
                    grouped_states[(state.index('1'),state.index('2'), state.index('8'))].append(list(state))
        return grouped_states
    
    def gen_states(self, elements='128xxx',num_dig=6):
        state_tuples = set(itertools.permutations(elements, num_dig))
        states = [list(state_tuple) for state_tuple in state_tuples]
        states.sort()
        return states
    # puzzle with m rows and n columns
    def Move(self,state_in, move,m=2,n=3):
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

class Env2_a2():
    def __init__(self,val='1'):
        self.val = val
        self.blank = '8'
        self.final_state = ['x', self.val, 'x', 'x', self.blank, 'x'] # not used but here for explicity
        elements = self.val + self.blank + 'xxxx'
        self.states = self.gen_states(elements=elements)
        self.tuple_grouped_states = self.tuple_grouped_3x3_states()
        self.grouped_states = self.grouped_states()
        
    def step(self, state_in, action,m=2,n=3):
        state = state_in.copy()
        done = False
        state = self.Move(state, action,m=m,n=n)
        reward = -1
        if m == 2 and n == 3:
            if state[1] == self.val and state[4] == self.blank:
                done = True
                reward = 1000
        if m == 3 and n == 3:
            if state[4] == self.val and state[7] == self.blank:
                done = True
                reward = 1000
        return state, reward, done
    # Return random state with all values in a state 'x' besides '0' and '8'
    def reset(self):
        return self.states[np.random.randint(len(self.states))]
    
    def get_group_index(self, state):
        for i in range(len(self.grouped_states)):
            if state in self.grouped_states[i]:
                return i

    def random_group_state(self):
        return self.grouped_states[np.random.randint(len(self.grouped_states))][np.random.randint(len(self.grouped_states[0]))]

    def grouped_states(self):
        state_list = [None] * 30
        for es in self.states:
            for key,item in self.tuple_grouped_states.items(): # key = index ; item = state
                if key == (self.convert_3x2_to_3x3(es.index(self.val)),self.convert_3x2_to_3x3(es.index(self.blank))):
                    state_list[self.states.index(es)] = item
        return state_list

    def convert_3x2_to_3x3(self,index):
        return index + 3

    def tuple_grouped_3x3_states(self):
        with open('solvable_states.txt','r') as file:
            states = file.readline()
        states = [x.strip(" '") for x in states.split(',')]
        grouped_states = defaultdict(list)
        for state in states:
            if state.index(self.val) != state.index(self.blank):
                if (state.index(self.val) >= 3) and (state.index(self.blank) >= 3):
                    grouped_states[(state.index(self.val), state.index(self.blank))].append(list(state))
        return grouped_states
    
    def gen_states(self, elements='18xxxx',num_dig=6):
        state_tuples = set(itertools.permutations(elements, num_dig))
        states = [list(state_tuple) for state_tuple in state_tuples]
        states.sort()
        return states
    # puzzle with m rows and n columns
    def Move(self,state_in, move,m=2,n=3):
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

