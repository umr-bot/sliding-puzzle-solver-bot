import numpy as np
from help_functions import *
# array of states, where each state is a scalar value
s = np.zeros(16) # a flattened 4x4 matrix representing a singular state
s = s.reshape(4,4)
a = np.arange(4) # action matrix to do with rewards

R = -1*np.ones(len(a)*s.shape[0]*s.shape[1]) # correction action by states
R = R.reshape(len(a),s.shape[0],s.shape[1])

P = np.zeros(len(a)*s.shape[0]*s.shape[1]*s.shape[0]*s.shape[1]) # actions by rows by cols by rows by cols 
P = P.reshape(len(a),s.shape[0],s.shape[1],s.shape[0],s.shape[1]) 
N = 4
for i in range(P.shape[0]):
    for j in range(P.shape[1]):
        if(i == 0): # first row (can't move up)
            P[0][i][j][i][j] = 1
        else: P[0][i][j][i-1][j] = 1 # other rows (can move up)
        
        if(i == P.shape[0]-1): # last row (can't move down)
            P[1][i][j][i][j] = 1
        else: P[1][i][j][i+1][j] = 1 # other rows (can move down)

        if(j == 0): # first column (can't move left)
            P[2][i][j][i][j] = 1
        else: P[2][i][j][i][j-1] = 1 # other columns (can move left)

        if(j == P.shape[1]-1): # last column (can't move right)
            P[3][i][j][i][j] = 1
        else: P[3][i][j][i][j+1] #other columns (can move right)
#for i in range(P.shape[0]):
#    for j in range(P.shape[1]):
#        set_action_matrix(P=P[i][j],block_index=i*4+j)
#        block_index = i*4 + j
#        if((block_index+1) > N): # up  # if(i == 0)
#            P[0][i][j] = 1 # P[0][i][j][i-1][j]
#        #else P[0][i][j][i][j] = 1
#        if(block_index+1) <= N*(N-1): # down
#            P[1][i][j] = 1
#        if((block_index+1) % N != 1): # left
#            P[2][i][j] = 1
#        if((block_index+1) % N > 0) : # right
#            P[3][i][j] = 1
        
p = P.reshape(N,s.shape[0]*s.shape[1],s.shape[0]*s.shape[1])
r = R.reshape(N,s.shape[0]*s.shape[1])
for i in range(N): 
    r[i][0] = 0 # set all rewards @ index 0 for all actions to zero
v = np.zeros(N**2) # initial value function value
#v = v.reshape(4,4)
v_kplus1 = np.ones(N**2)
#v_kplus1 = v_kplus1.reshape(4,4)
k = 0
diff = 10
#gamma = np.array([[0.5,0.5**2,0.5**3,0.5**4]]) # discount factor
#gamma = 0.5
#while diff > 0.001 and k<10000000: # loop through all blocks in grid
#    a = np.random.randint(4) #random action, up, down, left or right
#   max (a)
#    v = v_kplus1 # old v value at iteration k
#    v_kplus1 = R[a] + (gamma*P[a]*v_kplus1)
#    diff = np.linalg.norm(v_kplus1-v)
#    k += 1
#    #print("v:\n",v)
#    #print("v_kplus1:\n",v_kplus1)
#    #print(diff)

