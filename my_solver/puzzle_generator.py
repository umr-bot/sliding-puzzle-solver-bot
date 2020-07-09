import numpy as np

## Create an NxN sliding puzzle grid filled with randomly shuffled numbers
class puzzle(): 
 
    def __init__(self,N=4):
        self.N = N
        self.size  = N*N
        blocks = np.array(np.arange(1,self.size+1)) 
        self.blocks = blocks
        np.random.shuffle(self.blocks) 
        self.blank_index = np.where(self.blocks == (self.size))[0][0]

    # Switch pieces blank piece 16 up, down, left, or right if possible 
    def transpose(self,c='down'):
        blank_val = self.blocks[self.blank_index] # store initial blank value
        print("blank is at position",self.blank_index+1)
        flag = 1
        if(c == 'up'):
            if((self.blank_index+1) > self.N):
                i = self.blank_index - self.N
                flag = 0
            else: print("Not allowed to move up")
        if(c == 'down'):
            if(self.blank_index+1) <= self.N*(self.N-1):
                i = self.blank_index + self.N
                flag = 0
            else: print("Not allowed to move down")
        if(c == 'right'):
            if((self.blank_index+1) % self.N > 0) :
                i = self.blank_index + 1
                flag = 0
            else: print("Not allowed to move right")
        if(c == 'left'):
            if((self.blank_index+1) % self.N != 1):
                i = self.blank_index - 1
                flag = 0
            else: print("Not allowed to move left")
        if flag == 0 :
            self.blocks[self.blank_index] = self.blocks[i]
            self.blocks[i] = blank_val

            self.blank_index = np.where(self.blocks == (self.size))[0][0]
            print("blank is moved to position", self.blank_index+1)
