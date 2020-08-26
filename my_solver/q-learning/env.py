import numpy as np

class env():

    def __init__(self,state='0321',N=2):
        self.N = N
        self.state          = state
        self.final_state    = '1230' # 0 is blank block

    def step(self, action):
        
        new_state = self.transpose(move=action) # numpy array with grid size NxN
        ns = '' # new_state in string form eg. '0321' for terminal state
        for i in range(self.N**2):
            ns = ns + str(new_state[i])
        self.state = ns
        terminate = self.state == self.final_state # check if in terminal/final state
        reward = -1 # every step incurs reward of -1
        return self.state, reward, terminate

    def reset():
        pass
    
    # Switch pieces blank piece up, down, left, or right if possible 
    def transpose(self, move=0):
        size = self.N**2
        blocks = np.array([self.state[0],self.state[1],self.state[2],self.state[3]],dtype=int)
        blank = 0 # blank block is valued zero
        blank_index = np.where(blocks == blank)[0]
        flag = 1
        debug = 0 # active with 0
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

e = env()
up,down,left,right=0,1,2,3
print(e.step(down))
