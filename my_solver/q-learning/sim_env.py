import numpy as np
from help_functions import transpose, calc_reward
import itertools
from random import choices,rand
def greedy_exp(s,a,e=0.1):
    p = choices([0,1], [1-e,e]) # random action is represented by 1 with
                                # prob of e. While max action has prob of 1-e
    if p == 0: 
    if p == 1: a = np.randint(4) # random action
def sim(state,action,GRID_LEN=2):
    s_prime = transpose(blocks=state,move=action,N=GRID_LEN)   
    
    return s_prime

l=list(itertools.permutations('0123', 4))
all_states = np.array(l,dtype=np.int) # solvable and unsolvable states

m = all_states.astype(str).tolist()
m.sort()
a = [''.join(row) for row in m] # check end of this file to see output of n

N = len(a) # possible solvable states 4!/2. Total states including unsolvable is 4! = 24

