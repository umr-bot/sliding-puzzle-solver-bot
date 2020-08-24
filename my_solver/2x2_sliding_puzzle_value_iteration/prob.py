import numpy as np
import itertools
l=list(itertools.permutations('0123', 4))
all_states = np.array(l,dtype=np.int) # solvable and unsolvable states

m = all_states.astype(str).tolist()
m.sort()
a = [''.join(row) for row in m] # check end of this file to see output of n

N = len(a) # possible solvable states 4!/2. Total states including unsolvable is 4! = 24
blank_pos = np.zeros(N)
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == '3': blank_pos[i] = j
up, down, left, right = [],[],[],[]
for i in range(N):
    if blank_pos[i] == 0:
        down.append(a[i])
        right.append(a[i])
    if blank_pos[i] == 1: 
        down.append(a[i])
        left.append(a[i])
    if blank_pos[i] == 2: 
        up.append(a[i])
        right.append(a[i])
    if blank_pos[i] == 3:
        up.append(a[i])
        left.append(a[i])
P = np.zeros((4,N,N)) # actions x states x states
ROW_SIZE = COL_SIZE = 2
states = all_states
for i in range(N):
    for j in range(N):

            if blank_pos[i] < 2: P[0][i][i] = 1 # can not move up
            else:
                if np.sum(states[i] == states[j]) >= 2:
                    if np.where(states[i] == 3)[0][0]%2 == np.where(states[j] == 3)[0][0]%2 and states[i][]: # same col for blanks positions
                        P[0][i][j] = 1                # can move up
                else: P[0][i][i] = 1
    
    #if a[i] in up: P[i][new_state] = # what is new_state
    #else P[a][] = 1
# All the possible states for a 2x2 grid listed below: 
#['0123', '0132', '0213', '0231', '0312', '0321', '1023', '1032', '1203', '1230', '1302', '1320', '2013', '2031', '2103', '2130', '2301', '2310', '3012', '3021', '3102', '3120', '3201', '3210']

