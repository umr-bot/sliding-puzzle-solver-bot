import numpy as np
from help_functions import transpose

# A board is represented by a 1x(N*N) array where N = size of the board
sn = np.arange(1,17,1)  #blank block is the value 16 in this array representing
                        #final state
up,down,left,right = 0,1,2,3 # enumarate blank blocks possible movements
action = [up,down,left,right] # actions for blank block to move

s = np.array([5,1,2,3,13,6,7,4,16,15,10,8,14,11,12,9]) # start state

while (s != sn).any():
    a = down
    transpose(s,nove=action[a])

