import numpy as np
from help_functions import transpose, calc_reward
import itertools

l=list(itertools.permutations('0123', 4))
all_states = np.array(l,dtype=np.int) # solvable and unsolvable states

m = all_states.astype(str).tolist()
m.sort()
a = [''.join(row) for row in m] # check end of this file to see output of n

N = len(a) # possible solvable states 4!/2. Total states including unsolvable is 4! = 24
q = np.zeros((4,N))
while cur_s != a[0]:
    S = a[N-1] # initialize to 3210 for a 2x2 grid
    policy = 
    for step in range():

