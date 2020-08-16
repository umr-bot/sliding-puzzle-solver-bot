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
        else: P[3][i][j][i][j+1] = 1 #other columns (can move right)
# make down and right transitions from the zeroth block zero
# and instead then make transistions from the zeroth block to itself
# equal to 1 (value 1 represents possible movement)
P[1][0][0][0][0] = 1 
P[1][0][0][1][0] = 0
P[3][0][0][0][0] = 1
P[3][0][0][0][1] = 0
P[2][0][0][0][0] = 1
P[2][0][0][0][1] = 0
P[0][0][0][0][0] = 1
P[0][0][0][0][1] = 0

N = s.shape[0]*s.shape[1]
p = P.reshape(len(a),N,N)
r = R.reshape(len(a),N)
for i in range(len(a)): 
    r[i][0] = 0 # set all rewards @ index 0 for all actions to zero
v = np.zeros(N) # initial value function value
k = 0
diff = 10 # arbritary allocation larger than condition 0.001
gamma = 1 
while diff > 0.001 and k<10: # loop through all blocks in grid
    X = r + gamma*p.dot(v)
    v_kplus1 =  v
    v = np.amax(X,axis=0)
    
    diff = np.linalg.norm(v-v_kplus1)
    print(v.reshape(4,4))
    k += 1
    
