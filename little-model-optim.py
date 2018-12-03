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
import matplotlib.pyplot as plt
#from scipy import linalg, optimize
#from numpy import poly1d

####Advanced case##
### number of arrivals and departures (per hour) over 12-hour period.
##arrivals = [1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 0, 1]
##departures = [0, 0, 0, 1, 1, 1, 0, 1, 2, 0, 2, 2]
##
### calculate average L and lam.
##tot_arr = np.cumsum(arrivals)
##tot_dep = np.cumsum(departures)
##
##L = np.mean(tot_arr - tot_dep)
##lam = np.mean(arrivals)
##W = L/lam
##
##print(W)

##Expert case##

# set up dictionaries to save keys (simulation #) and values (simulated values)
lamdict={}
Ldict={}
Wdict={}            

##for i in range (1,11):              # set number of simulations
    ##lam = np.random.poisson(5.0)    # simulate arrival rate by Poisson distribution
for lam in range(1,11):             # Assume different arrival rates lam.
    for L in range(10,26):          # Assume L varies in size, from e.g. 10 to 25
        W = L/float(lam)
        lamdict.setdefault(lam,[]).append(lam)
        Ldict.setdefault(lam,[]).append(L)
        Wdict.setdefault(lam,[]).append(W)

# plot for each L, W for lam.
for i in r:
    lamplot = lamdict[2][i]
    Wplot = Wdict[2][i]
    print lamplot
    sys.end(0)

print (lamplot)
print(Wplot)

plt.plot(Wplot,lamplot)
plt.ylabel('waiting time')
plt.xlabel('arrival rate')
plt.show()

# beds = np.arange(1,21)              # define the possible number of beds (1-20, here)

# ?simulated case: start with zero occupied beds, and assume end with zero.
# los = 8                 # define average LOS for maternity: approx 8 days, depending on type of delivery, world region: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4783077/
