import numpy as np
import itertools
#def num_inversions(blocks,blank_index=4,size=4):
#    inversions = 0
#    for i in range(size-1): # exclude last block, hence minus 1
#        for j in range(i+1,size): # start scanning one index past i
#            if i != blank_index and blocks[i] > blocks[j]:
#                inversions += 1
#    return inversions
#
## Determines if an NxN sliding puzzle is solvable, returns True if it is
#def is_solvable(state,N=2):
#    blank_index = np.where(state == ((N**2) -1))[0][0]
#    if N % 2 == 1: # check if odd
#        if num_inversions(state) % 2 == 0: # check if num_inversions is even
#            return True
#    if N % 2 == 0: # check if even
#        blank_row = int(blank_index / N
#        # check if num_inversions plus the row the blank is on is odd
#        if (num_inversions(state)+blank_row) % 2 == 1:
#            return True
#    return False

    #must still fix:  s = np.array([0,3,2,1])
    #must still fix:  #N = np.math.factorial(len(st still fix) # this is the amount of possible states
    #must still fix:  
    #must still fix:  l=list(itertools.permutations('0123', 4))
    #must still fix:  la = np.array(lt still fix.astype('int')
    #must still fix:  #st still fixlvable_states = np.empty([3,4])
    #must still fix:  ss = []
    #must still fix:  for state in lt still fix:
    #must still fix:      if is_solvable(state): st still fix.append(state)
    #must still fix:  
solvable = np.array([   [0,1,2,3],[1,3,0,2],[3,2,1,0],[2,0,3,1],
                        [0,1,3,2],[1,2,0,3],[2,3,1,0],[3,0,2,1],
                        [0,3,2,1],[3,1,0,2],[1,2,3,0],[2,0,1,3] ])

### returns a list of numbers formed by concatenating elements of the input
### array state
def encoder(state):
    state_list = state.astype(str).tolist()
    state_list.sort()
    return [''.join(row) for row in state_list]
### repeating what is being done in the encoder function temporarily to be explicit
m = solvable.astype(str).tolist()
m.sort()
n = [''.join(row) for row in m] # check end of this file to see output of n

N = 12 # possible solvable states 4!/2. Total states including unsolvable is 4! = 24
blank_pos = np.zeros(N).reshape(N,1)
for i in range(len(n)): 
    for j in range(len(n[0])): 
        if n[i][j] == '3': blank_pos[i] = j

up,down,left,right = [],[],[],[] # sets indicate states which can move in these 
                                 # directions
states = np.array(m).astype(int)
a = [0,1,2,3]
P = np.zeros((4,N,N))
for i in range(N):
    for j in range(N):
        
            if blank_pos[i][0] < 2: P[0][i][i] = 1 # can not move up
            else:
                if np.sum(states[i] == states[j]) >= 2:
                    if np.where(states[i] == 3)[0][0]%2 == np.where(states[j] == 3)[0][0]%2: # same col for blanks positions
                        P[0][i][j] = 1                # can move up

            if blank_pos[i][0] >= 2: P[1][i][i] = 1 # can not move down
            else: 
                if np.sum(states[i] == states[j]) >= 2:
                    if np.where(states[i] == 3)[0][0]%2 == np.where(states[j] == 3)[0][0]%2: # same row for blanks positions

                        P[1][i][j] = 1                 # can move down

            if blank_pos[i][0] % 2 == 0: P[2][i][i] = 1 # can not move left
            else: 
                if np.sum(states[i] == states[j]) >= 2:
                    if (np.where(states[i] == 3)[0][0]<2 and np.where(states[j] == 3)[0][0]<2) or (np.where(states[i] == 3)[0][0] >= 2 and np.where(states[j] == 3)[0][0] >= 2): # same row for blanks positions
                        P[2][i][j] = 1                     # can move left

            if blank_pos[i][0] % 2 == 1: P[3][i][i] = 1 # can not move right
            else: 
                if np.sum(states[i] == states[j]) >= 2:
                    if (np.where(states[i] == 3)[0][0]<2 and np.where(states[j] == 3)[0][0]<2) or (np.where(states[i] == 3)[0][0] >= 2 and np.where(states[j] == 3)[0][0] >= 2): # same row for blanks positions

                        P[3][i][j] = 1                     # can move right

P[0][0][3] = 0 #'blank up' possible but make it zero since in terminal state
P[2][0][1] = 0 #'blank right' possible but make it zero since in terminal state
#################

R = -1*np.ones(len(a)*N).reshape(len(a),N)
for i in range(len(a)): 
    R[i][0] = 0 # set all rewards @ index 0 for all actions to zero
v = np.zeros(N) # initial value function value
k = 0
diff = 10 # arbritary allocation larger than condition 0.001
gamma = 1
arr = []
while diff > 0.001 and k<1000: # loop through all blocks in grid
    X = R + gamma*P.dot(v)
    v_kplus1 =  v
    arr.append(v_kplus1)
    v = np.amax(X,axis=0)
    
    diff = np.linalg.norm(v-v_kplus1)
#    print(v.reshape(4,4))
    k += 1
    
### Solvable states ###
#[['0', '1', '2', '3'],
# ['0', '1', '3', '2'],
# ['0', '3', '2', '1'],
# ['1', '2', '0', '3'],
# ['1', '2', '3', '0'],
# ['1', '3', '0', '2'],
# ['2', '0', '1', '3'],
# ['2', '0', '3', '1'],
# ['2', '3', '1', '0'],
# ['3', '0', '2', '1'],
# ['3', '1', '0', '2'],
# ['3', '2', '1', '0']]
#OR
# ['0123',
# '0132',
# '0321',
# '1203',
# '1230',
# '1302',
# '2013',
# '2031',
# '2310',
# '3021',
# '3102',
# '3210']
