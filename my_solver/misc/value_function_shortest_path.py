import numpy as np
from help_functions import *
# array of states, where each state is a scalar value
s = np.zeros(16) # a flattened 4x4 matrix representing a singular state
s = s.reshape(4,4)
a = np.arange(4) # action matrix to do with rewards

R = -1*np.ones(len(a)*len(s)*len(s))
R = R.reshape(len(a),s.shape[0],s.shape[1])
R[0][0][0] = 0

P = np.zeros(len(a)*len(s)*len(s))  
P = P.reshape(len(a),s.shape[0],s.shape[1]) 
N = 4
for i in range(P.shape[0]):
    for j in range(P.shape[1]):
        set_action_matrix(P=P[i][j],block_index=i*4+j)
        block_index = i*4 + j
        if((block_index+1) > N): # up
            P[0][i][j] = 1
        if(block_index+1) <= N*(N-1): # down
            P[1][i][j] = 1
        if((block_index+1) % N != 1): # left
            P[2][i][j] = 1
        if((block_index+1) % N > 0) : # right
            P[3][i][j] = 1
        
### Old none working probility matrix initialization
#P = np.ones(len(a)*len(s)*len(s))  
#P = P.reshape(len(a),s.shape[0],s.shape[1]) 
#for i in range(P.shape[0]): # rows
#        for j in range(P.shape[1]): # columns
#            for k in range(P.shape[2]): # actions: up,down,left,right
#                if i==0 and j>0 and (j<P.shape[1]-1): # top middle row
#                    P[i][j][k] = 0
#                if (i==P.shape[0]-1) and j>0 and (j<P.shape[1]-1): # bottom middle row
#                    P[i][j][k] = 0
#                if j==0 and i>0 and (i<P.shape[0]-1): # left middle column
#                    P[i][j][k] = 0
#                if (j==P.shape[1]-1) and i>0 and (i<P.shape[0]-1): # right middle column
#                    P[i][j][k] = 0

#print("up action probibility matrix\n",P)
#print("down action probibility matrix\n",P[1])
#print("left action probibility matrix\n",P[2])
#print("right action probibility matrix\n",P[3])
p = P.reshape(4,16)
r = R.reshape(4,16)
v = np.zeros(16) # initial value function value
#v = v.reshape(4,4)
v_kplus1 = np.ones(16)
#v_kplus1 = v_kplus1.reshape(4,4)
k = 0
diff = 10
#gamma = np.array([[0.5,0.5**2,0.5**3,0.5**4]]) # discount factor
#gamma = 0.5
#while diff > 0.001 and k<10000000: # loop through all blocks in grid
#    a = np.random.randint(4) #random action, up, down, left or right
#    v = v_kplus1 # old v value at iteration k
#    v_kplus1 = R[a] + (gamma*P[a]*v_kplus1)
#    diff = np.linalg.norm(v_kplus1-v)
#    k += 1
#    #print("v:\n",v)
#    #print("v_kplus1:\n",v_kplus1)
#    #print(diff)

