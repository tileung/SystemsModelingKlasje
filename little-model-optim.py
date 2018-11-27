## Purpose: 
## (1) Modeling of a single queuing system using the example of Little;
## (2) the occupancy rate chance at different states of the system and
## the effect of adding an extra workstation on occupancy rate.

## L = (known) avg number of items in the system
## W = avg waiting time in the system for an item
## lam = (known) avg number of items arriving per hour

## Little's law: W = L/lam

import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from scipy import linalg, optimize
#from numpy import poly1d

##Advanced case##
# number of arrivals and departures (per hour) over 12-hour period.
arrivals = [1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 0, 1]
departures = [0, 0, 0, 1, 1, 1, 0, 1, 2, 0, 2, 2]

# calculate average L and lam.
tot_arr = np.cumsum(arrivals)
tot_dep = np.cumsum(departures)

L = np.mean(tot_arr - tot_dep)
lam = np.mean(arrivals)
W = L/lam

print(W)

