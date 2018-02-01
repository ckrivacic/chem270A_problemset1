import sys
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import binom

"""
First argument should be number of steps. 
"""
Nstep = [4,16,32]
Ntrial = 100

averages = {}
for steps in Nstep:
    averages[steps] = []

for i in range(0,Ntrial):
    for steps in Nstep:
        randn_collector = []
        for j in range(0,steps):
            randn = random.uniform(0,1)
            randn_collector.append(randn)
        averages[steps].append(sum(randn_collector) /
        float(len(randn_collector)))
print averages

"""
probability = numerator / float(num_trials)
print "Probability that virus will be destroyed:"
print probability
"""
plt.subplot(311)
plt.hist(averages[4])
plt.title('Distribution of averages for Nstep=4')
plt.ylabel('Frequency')
#plt.xlabel('Average')

plt.subplot(312)
plt.hist(averages[16])
plt.title('Distribution of averages for Nstep=16')
plt.ylabel('Frequency')
#plt.xlabel('Average')

plt.subplot(313)
plt.hist(averages[32])
plt.title('Distribution of averages for Nstep=32')
plt.ylabel('Frequency')
plt.xlabel('Average')

plt.show()

