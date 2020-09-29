import numpy as np
import itertools

class env():

    def __init__(self,state='3210',N=2):
        self.N = N
        self.state           = state
        self.final_state     = '0123' # 0 is blank block
        self.blank           = '3'
        self.blank_index     = self.state.index(self.blank)
        self.states          = self.gen_states()
        self.solvable_states = self.get_solvable_states()
    def step(self, action):
        
        self.state = self.transpose(move=action) # numpy array with grid size NxN
        terminate = self.state == self.final_state # check if in terminal/final state
        if terminate:   reward = 100
        else:           reward = -1 # every step incurs reward of -1
        return self.state, reward, terminate

    def reset(self):
        rand            = np.random.randint(len(self.solvable_states))
        self.state      = self.solvable_states[rand]
        return self.state
    
    # write out actions made to a file
    def render(self):
        with open("actions.txt", "w+") as file1:
            file1.write(self.state+'\n')
            if self.state == self.final_state: file1.write("Done"+'\n')

    # Switch pieces blank piece up, down, left, or right if possible 
    def transpose(self, move=0):
        size = self.N**2
        self.blank_index = self.state.index(self.blank) # get postion of '0'
        flag = 1
        debug = 1 # active with 0
        if(move == 0):
            if((self.blank_index+1) > self.N):
                i = self.blank_index - self.N
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move up")
        if(move == 1):
            if(self.blank_index+1) <= self.N*(self.N-1):
                i = self.blank_index + self.N
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move down")
        if(move == 2):
            if((self.blank_index+1) % self.N != 1):
                i = self.blank_index -  1
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move left")
        if(move == 3):
            if((self.blank_index+1) % self.N > 0) :
                i = self.blank_index + 1
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move right")
        if flag == 0 : # if move is possible
            state = self.state[:self.blank_index] + self.state[i] + self.state[self.blank_index+1:]
            self.state = state[:i] + self.blank + state[i+1:]
            self.blank_index = self.state.index(self.blank)
            if debug == 0: print("blank is moved to position", self.blank_index+1)
            return self.state
        else: return self.state
    
    # Returns list of a sliding puzzle grids as flattened NxN lists
    def gen_states(self):
        l=list(itertools.permutations('0123', 4))
        state_list = [''.join(row) for row in l]
        return state_list

    # Determines if an NxN sliding puzzle is solvable, returns True if it is
    # obtain all solvable states which is length N!/2
    def get_solvable_states(self):
        cnt = 0
        states = self.gen_states()
        solvable_states = []
        for s in states:
            self.state = s
            if self.is_solvable():
                solvable_states.append(s)
                cnt += 1 
        return solvable_states

    def is_solvable(self):
        self.blank_index = self.state.index(self.blank)
        if self.N % 2 == 1: # check if odd
            if self.num_inversions() % 2 == 0: # check if num_inversions is even
                return True
        if self.N % 2 == 0: # check if even
            blank_row = int(self.blank_index / self.N)
            # check if num_inversions plus the row the blank is on is odd
            if (self.num_inversions()+blank_row) % 2 == 1:
                return True

        return False

    def num_inversions(self):
        self.blank_index = self.state.index(self.blank)
        inversions = 0
        size = self.N**2
        for i in range(size): # exclude blank, hence minus 1
            #print("i",i)
            #print("self.state[i]",self.state[i])
            for j in range(i+1,size): # start scanning one index past i
                #print("self.state[j]",self.state[j])
                if i != self.blank_index and int(self.state[i]) > int(self.state[j]):
                    inversions += 1
                    #print("inversions",inversions)
        return inversions

################ Test of class #################
#e = env()
#up,down,left,right=0,1,2,3
#e.reset()
#print(e.state)
#print("number of inversions",e.num_inversions())
###############################################################
