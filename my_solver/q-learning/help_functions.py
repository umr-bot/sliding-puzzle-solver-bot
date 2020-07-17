import numpy as np

# Calculates total reward associated with making a singular action
def calc_reward(s):
    sn = np.arange(1,17,1)  #blank block is the value 16 in this array representing
    #s = np.array([5,1,2,3,13,6,7,4,16,15,10,8,14,11,12,9]) # start state
    tot_reward = 0 # make reward directly the sum of the taxi_distances
    j=0 # j is the y value the board with origin at left bottom corner
    #s = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    for i in range(len(s)): # for every block in the board in state s
        if i==3: i=0
        if j==3: j=0
        taxi_dist = np.abs(s[i] - sn[i]) + np.abs(s[j] - sn[j])
        tot_reward += taxi_dist
        j += 1
    return tot_reward

# Switch pieces blank piece 16 up, down, left, or right if possible 
def transpose(blocks, move=0,N=4):
    size = N*N
    blank_index = np.where(blocks == (size))[0][0]
    flag = 1
    debug = 0
    if(move == 0):
        if((blank_index+1) > N):
            i = blank_index - N
            flag = 0
        else: 
            if debug == 0: print("Not allowed to move up")
    if(move == 1):
        if(blank_index+1) <= N*(N-1):
            i = blank_index + N
            flag = 0
        else: 
            if debug == 0: print("Not allowed to move down")
    if(move == 2):
        if((blank_index+1) % N != 1):
            i = blank_index - 1
            flag = 0
        else: 
            if debug == 0: print("Not allowed to move left")
    if(move == 3):
        if((blank_index+1) % N > 0) :
            i = blank_index + 1
            flag = 0
        else: 
            if debug == 0: print("Not allowed to move right")
    if flag == 0 :
        blocks[blank_index] = blocks[i]
        blocks[i] = size

        blank_index = np.where(blocks == (size))[0][0]
        if debug == 0: print("blank is moved to position", blank_index+1)
        return 0,blocks # returning 0 indicates a valid move has been made
    else: return 1,blocks # returning 1 indicates an invalid move

