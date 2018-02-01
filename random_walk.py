import sys
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import binom

"""
First argument should be number of steps. 
"""
num_steps = int(sys.argv[1])
num_trials = int(sys.argv[2])

points_visited = []

numerator = 0
for i in range(0, num_trials):
    position = -4
    destroyed = False
    for i in range(0,num_steps):
        randn = random.uniform(0,1)
        if randn < 0.65:
            position += 1
        else:
            position -=1
        print position
        points_visited.append(position)
        if position == 0:
            print("Virus destroyed")
            destroyed = True
            break
    if destroyed==True:
        numerator += 1

probability = numerator / float(num_trials)
print "Probability that virus will be destroyed:"
print probability

plt.subplot(211)
plt.hist(points_visited)
plt.title('Histogram of lattice points visited')
plt.ylabel('Frequency')
plt.xlabel('Lattice point')

#Binomial setup
n, p = 100, 0.84
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))

#Binomial plot
plt.subplot(212)
plt.bar(x, binom.pmf(x, n, p))
plt.title('Plot of binomial distribution of successes for p=0.84, n=100')
plt.xlabel('# of successes after 100 trials')
plt.ylabel('Probability')

plt.show()
