import numpy as np
import itertools
class env():

    def __init__(self,state='087654321',N=3):
        self.N = N
        self.state          = state
        self.final_state    = '123456780' # 0 is blank block
        self.states         = self.gen_states()

    def step(self, action):
        
        new_state = self.transpose(move=action) # numpy array with grid size NxN
        ns = '' # new_state in string form eg. '0321' for terminal state
        for i in range(self.N**2):
            ns = ns + str(new_state[i])
        self.state = ns
        terminate = self.state == self.final_state # check if in terminal/final state
        reward = -1 # every step incurs reward of -1
        return self.state, reward, terminate

    def reset(self):
        #solvable_states = [ '0123','1302','3210','2031',
        #                '0132','1203','2310','3021',
        #                '0321','3102','1230','2013' ]
        
        rand = np.random.randint(len(self.states))
        self.state = self.states[rand]
        return self.state
    
    # write out actions made to a file
    def render(self):
        with open("actions.txt", "w+") as file1:
            file1.write(self.state+'\n')
            if self.state == self.final_state: file1.write("Done"+'\n')

    # Switch pieces blank piece up, down, left, or right if possible 
    def transpose(self, move=0):
        size = self.N**2
        blocks = np.array([self.state[0],self.state[1],self.state[2],self.state[3],self.state[4],self.state[5],self.state[6],self.state[7],self.state[8]],dtype=int)
        blank = 0 # blank block is valued zero
        blank_index = np.where(blocks == blank)[0]
        flag = 1
        debug = 1 # active with 0
        if(move == 0):
            if((blank_index+1) > self.N):
                i = blank_index - self.N
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move up")
        if(move == 1):
            if(blank_index+1) <= self.N*(self.N-1):
                i = blank_index + self.N
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move down")
        if(move == 2):
            if((blank_index+1) % self.N != 1):
                i = blank_index - 1
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move left")
        if(move == 3):
            if((blank_index+1) % self.N > 0) :
                i = blank_index + 1
                flag = 0
            else: 
                if debug == 0: print("Not allowed to move right")
        if flag == 0 :
            blocks[blank_index] = blocks[i]
            blocks[i] = blank

            blank_index = np.where(blocks == blank)[0]
            if debug == 0: print("blank is moved to position", blank_index+1)
            return blocks # returning 0 indicates a valid move has been made
        else: return blocks # returning 1 indicates an invalid move
    
    # Returns list of a sliding puzzle grids as flattened NxN lists
    def gen_states(self):
        l=list(itertools.permutations('012345678', 9))
        all_states = np.array(l,dtype=np.int) # solvable and unsolvable states

        m = all_states.astype(str).tolist()
        m.sort()
        state_list = [''.join(row) for row in m]
        N = len(state_list) # possible solvable states 9!/2. Total states including unsolvable is 9! = 362880
        return state_list
################ Test of class #################
#e = env()
#up,down,left,right=0,1,2,3
#print(e.step(down))

###############################################################

