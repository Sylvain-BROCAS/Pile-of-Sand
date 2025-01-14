import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import repeat  
import seaborn as sns
from matplotlib.animation import FuncAnimation, ArtistAnimation
from random import randint

# Simulation settings
size = (10,10) #Map size (n_col, n_lines) # Size of the grid
n_terms = 500 # Number of simulation steps
critic_ng = 4 # Critical threshold (max nb of grains per cell)


sand_map = np.zeros(size) # Map initialisation

def avalanche(map):
    print("-"*75, "\n>>> ", i)

    # Randomly add a new grain on the grid
    m,n = randint(0,size[0]-1), randint(0,size[1]-1)
    #print("A grain of sand was droped here : (", m, ", ", n, ")")
    new_grain = np.zeros(size)
    new_grain[m,n] += 1
    map += new_grain

    # Scan of the grid to find where there are too many grains
    for m in range(size[0]):
        for n in range(size[1]):
            #print("--> Checking for avalanche here : (", m, ", ", n, ")")
            # If a cell contains more grains than the critical threshold, these grains are moved to the cells around
            if map[m, n] >= critic_ng:
                map[m, n] -= critic_ng
                if m+1 < size[0]:
                    map[m+1, n] += critic_ng //4
                if m-1 >= 0:
                    map[m-1, n] += critic_ng //4
                if n+1 < size[1]:
                    map[m, n+1] += critic_ng //4
                if n-1 >= 0:
                    map[m, n-1] += critic_ng //4
    # print(map)
    return map

map = sand_map
frames = [] # A list to stock all the simulation steps
for i in range(n_terms):
    frames.append((plt.pcolor(map),))
    map = avalanche(map)

# Animation
fig = plt.figure()
anim = ArtistAnimation(fig, frames, interval = 100, blit = True, repeat = False, repeat_delay = 1000)
plt.show()
