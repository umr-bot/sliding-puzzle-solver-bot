import numpy as np

# array of states, where each state is a scalar value
s = np.zeros(16) # a flattened 4x4 matrix representing a singular state
s = s.reshape(4,4)
a = np.arange(4) # action matrix to do with rewards

R = -1*np.ones(len(a)*len(s)*len(s))
R = R.reshape(len(a),s.shape[0],s.shape[1])
R[0][0][0] = 0

P = np.ones(len(a)*len(s)*len(s))  
P = P.reshape(len(a),s.shape[0],s.shape[1]) 
for i in range(P.shape[0]): # rows
        for j in range(P.shape[1]): # columns
            for k in range(P.shape[2]): # actions: up,down,left,right
                if i==0 and j>0 and (j<P.shape[1]-1): # top middle row
                    P[i][j][k] = 0
                if (i==P.shape[0]-1) and j>0 and (j<P.shape[1]-1): # bottom middle row
                    P[i][j][k] = 0
                if j==0 and i>0 and (i<P.shape[0]-1): # left middle column
                    P[i][j][k] = 0
                if (j==P.shape[1]-1) and i>0 and (i<P.shape[0]-1): # right middle column
                    P[i][j][k] = 0

#print(P)
print("up action probibility matrix\n",P[0])
print("down action probibility matrix\n",P[1])
print("left action probibility matrix\n",P[2])
print("right action probibility matrix\n",P[3])

#for i in range(len(s)*len(s)): # loop through all blocks in state
    
### initialize code that doesnt work properly yet
#R = np.zeros((len(a),s.shape[0],s.shape[1])) 
#for i in range(len(a)): 
#    for j in range(s.shape[0]): 
#        for k in range(s.shape[1]): 
#            R[a][j][k] = -1 
#            print(R[a][j][k]) 

#def check_max_neighbour_blocks(s,block_index):
#    max_val = -1000000
#    ### TODO check if N is odd if the modulus logic still works
#    # First block could also be coded as if block_index == 0""
#    if block_index+1 < N and (block_index+1)%N == 1:
#        # calc max of right and down values
#        pass
#    elif block_index+1 > N and (block_index+1)%N == 1:
        
        
