## Purpose: 
## (1) Modeling of a single queuing system using the example of Little;
## (2) the occupancy rate chance at different states of the system and
## the effect of adding an extra workstation on occupancy rate.

## L = (known) avg number of items/patients in the queuing system/waiting room +
     # number of workstations/available providers to see patients
## W = avg waiting time in the system for an item/patient
## lam = (known) avg number of items/patients arriving PER UNIT TIME

import decimal
D=decimal.Decimal

## Part 1: Define functions ##
##############################

def waittimecalc(workstations, queue, lam):
    # user-entereed values for number of workstations available, number of patients in queue, & avg arrival rate)
    # calculate average waiting time
    L = D(workstations) + D(queue)
    W = L / lam
    print 'Average waiting time in the system for each patient'
    print W

# test call: waittimecalc(4, 16, 16)

def queuecalc(workstations, W, lam):
    Lq = 0
    Lw = D(lam) * D(W)              # number of patients at in process; cannot be >workstations
    if Lw > workstations:
        Lq = Lw - workstations    # number of patients in queue    
    elif Lw == workstations:
        Lq = 0
    print 'Number of patients waiting in queue'
    print Lq

# test call: queuecalc(4, 0.5, 16)


## Part 2: Calculate occupancy rate (probability) given different states of the system. ##
##########################################################################################
## in progres ##
################

# generate random number of possible arriving patients, per hour.
import random

workstations = random.randint(1,4)  # assume at least 1 workstation is open, maximum of 4
W = 0.5
lam = random.randint(1,16)          # assume at least 1 patient arrives per hour (otherwise no clinic)

print workstations
print lam
queuecalc(workstations, W, lam)
