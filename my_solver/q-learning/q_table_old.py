import numpy as np
from help_functions import transpose, calc_reward
N = 2
size = N*N
# A board is represented by a 1x(N*N) array where N = size of the board
sn = np.arange(1,10,1)  #blank block is the value 16 in this array representing
                        #final state
                        #make sure calc_rewards function has correct sn
up,down,left,right = 0,1,2,3 # enumarate blank blocks possible movements
#action = [up,down,left,right] # actions for blank block to move

#s = np.array([5,1,2,3,13,6,7,4,16,15,10,8,14,11,12,9]) # start state
s = np.array([1,2,3,4,9,5,7,8,6])
a = 1 # randomly allocate a and a_old
a_old = 0
s_old = s
while (s != sn).any():
    blank_index = np.where(s == (size))[0][0]
    r = 0
    if((blank_index+1) > N): # up
        valid_move,temp_s = transpose(s,move=up,N=N) # update s if valid move
        temp_r = calc_reward(temp_s)
        print("up:",temp_r)
        if np.max([temp_r,r]) == 0:
            s = sn
            continue
        r = 1/float(np.max([temp_r,r]))
        if temp_r > r:
            a = 0
            r = temp_r
       
    if(blank_index+1) <= N*(N-1): # down
        valid_move,temp_s = transpose(s,move=down,N=N) # update s if valid move
        temp_r = calc_reward(temp_s)
        print("down:",temp_r)
        if np.max([temp_r,r]) == 0:
            s = sn
            continue
        r = 1/float(np.max([temp_r,r]))
        if temp_r > r: 
            a = 1
            r = temp_r

    if((blank_index+1) % N != 1): # left
        valid_move,temp_s = transpose(s,move=left,N=N) # update s if valid move
        temp_r = calc_reward(temp_s)
        print("left:",temp_r)
        if np.max([temp_r,r]) == 0:
            s = sn
            continue
        r = 1/float(np.max([temp_r,r]))
        if temp_r > r: 
            a = 1
            r = temp_r

    if((blank_index+1) % N > 0) : # right
        valid_move,temp_s = transpose(s,move=right,N=N) # update s if valid move
        temp_r = calc_reward(temp_s)
        print("right:",temp_r)
        if np.max([temp_r,r]) == 0:
            s = sn
            continue
        r = 1/float(np.max([temp_r,r]))
        if temp_r > r: 
            a = 3
            r = temp_r
    
    if (s != s_old).any(): continue  # dont move back to the same place ever
    a_old = a
    s_old = s
    valid_move,s = transpose(s,move=a,N=N) # update s if valid move
    print(s)
    print(r)

