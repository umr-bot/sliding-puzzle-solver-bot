import numpy as np
from help_functions import *
# array of states, where each state is a scalar value
s = np.zeros(16) # a flattened 4x4 matrix representing a singular state
s = s.reshape(4,4)
a = np.arange(4) # action matrix to do with rewards with order:
                 # up, down, left, right
R = -1*np.ones(len(a)*s.shape[0]*s.shape[1]) # correction action by states
R = R.reshape(len(a),s.shape[0],s.shape[1])

P = np.zeros(len(a)*s.shape[0]*s.shape[1]*s.shape[0]*s.shape[1]) # actions by rows by cols by rows by cols 
P = P.reshape(len(a),s.shape[0],s.shape[1],s.shape[0],s.shape[1])
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
N = s.shape[0]*s.shape[1]
p = P.reshape(len(a),N**2)
r = R.reshape(len(a),N)
for i in range(len(a)): 
    r[i][0] = 0 # set all rewards @ index 0 for all actions to zero
v = np.zeros((N,1)) # initial value function value
v_kplus1 = np.ones((N,1)) # this case 16x1
k = 0
diff = 10 # arbritary allocation larger than condition 0.001
gamma = 1 
while diff > 0.001 and k<10000: # loop through all blocks in grid
    #if k < 1: v = v_kplus1 # old v value at iteration k
    #else: 
    #    v = v_kplus1.T
    #    print(v_kplus1.T.shape)
    v = v_kplus1 # old v value at iteration k
    pa = np.amax(p,axis=0)
    ra = np.amax(r,axis=0)
    # note pa.dot(v_kplus1) result has dimension 1x16
    # hence encase np.max(r,axis=0) with an array
    if k <= 0: temp = pa.reshape(N,N).dot(v_kplus1).T
    else: temp = pa.reshape(N,N).dot(v_kplus1.T).T
    v_kplus1 = ra + gamma*temp
    diff = np.linalg.norm(v_kplus1-v)
    k += 1
    #print("v:\n",v)
    #print("v_kplus1:\n",v_kplus1)
    #print(diff)

