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
solvable = np.array([[0,1,2,3],[1,3,0,2],[3,2,1,0],[2,0,3,1],[0,1,3,2],[1,2,0,3],[2,3,1,0],[3,0,2,1],[0,3,2,1],[3,1,0,2],[1,2,3,0],[2,0,1,3]])

### returns a list of numbers formed by concatenating elements of the input
### array state
def encoder(state):
    state_list = state.astype(str).tolist()
    state_list.sort()
    return [''.join(row) for row in state_list]

m = solvable.astype(str).tolist()
m.sort()
n = [''.join(row) for row in m]

look_up = np.zeros(12).reshape(12,1) 
for i in range(len(n)): 
    for j in range(len(n[0])): 
        if n[i][j] == '3': look_up[i] = j
P = np.zeros((12,12))
for i in range(look_up.shape[0]): # look_up.shape[0] = 4!/2 = 12 for a 2x2 puzzle
    for j in range(look_up.shape[0]):
        if np.abs(look_up[i]-look_up[j]) == 1: # pos3(state) - pos3(state + i) i in [0,N-1],N=2
            P[i][j] = 1
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
