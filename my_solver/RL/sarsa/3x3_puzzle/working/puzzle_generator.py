import numpy as np

## Create an NxN sliding puzzle grid filled with randomly shuffled numbers
class puzzle(): 

    def __init__(self,N=4):
        self.debug = 1
        self.N = N
        self.size  = N*N
        self.blocks = np.array(np.arange(1,self.size+1)) 
        self.blank_index = np.where(self.blocks == (self.size))[0][0]


    # Make a solvable solvable puzzle and output it as an 1x(N*N) array
    def generate_puzzle(self,state=[]):
        if state == []:
            i = 0
            while i < 200:
                # check if a valid move is made, if it is increment i
                if self.transpose(move=np.random.randint(self.N)) == 0: i+=1
        self.blocks = state
        self.blank_index = np.where(self.blocks == (self.size))[0][0]
 

    # Switch pieces blank piece 16 up, down, left, or right if possible 
    def transpose(self,move=0):
        blank_val = self.blocks[self.blank_index] # store initial blank value
        if self.debug == 0: print("blank is at position",self.blank_index+1)
        flag = 1
        if(move == 0):
            if((self.blank_index+1) > self.N):
                i = self.blank_index - self.N
                flag = 0
            else: 
                if self.debug == 0: print("Not allowed to move up")
        if(move == 1):
            if(self.blank_index+1) <= self.N*(self.N-1):
                i = self.blank_index + self.N
                flag = 0
            else: 
                if self.debug == 0: print("Not allowed to move down")
        if(move == 2):
            if((self.blank_index+1) % self.N != 1):
                i = self.blank_index - 1
                flag = 0
            else: 
                if self.debug == 0: print("Not allowed to move left")
        if(move == 3):
            if((self.blank_index+1) % self.N > 0) :
                i = self.blank_index + 1
                flag = 0
            else: 
                if self.debug == 0: print("Not allowed to move right")
        if flag == 0 :
            self.blocks[self.blank_index] = self.blocks[i]
            self.blocks[i] = blank_val

            self.blank_index = np.where(self.blocks == (self.size))[0][0]
            if self.debug == 0: print("blank is moved to position", self.blank_index+1)
            return 0 # returning 0 indicates a valid move has been made
        else: return 1 # returning 1 indicates an invalid move
    
### Uncomment below to test the class
#p = puzzle()
#p.generate_puzzle()
#print(p.num_inversions())
