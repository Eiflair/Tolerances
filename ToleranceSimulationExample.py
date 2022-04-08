# -*- coding: utf-8 -*-
"""
@author: Tim Brix Nerenst,
         TBNE@MEK.DTU.DK

The folling script performs a Monte Carlo simulation.
The goal is to investigate how variation impacts the fit/interference of 4 boxes (3 inner, 1 outer).
"""
# Packages imported (used for calculations in below)
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

# Define the nominal size and variation (sigma value) of the three inner boxes
boxA, sigA  = 5, 0.1/1
boxB, sigB  = 7, 0.1/1
boxC, sigC  = 10, 0.1/1

# Define the nominal size and variation (sigma value) of the outer box
boxD, sigD  = 22, 0.1/1

# Define the production size
prodSize = 10000

# Define fuction for generating production parts
# 'mu' is the nominal size 
# 'sig' is the sigma value 
# 'size' is the size of production
def prodPart(mu,sig,size):
    prod = np.random.normal(mu,sig,size) #normal distribution
    return prod

# Calculate the box dimensions with variation included
prodA = prodPart(boxA, sigA, prodSize)
prodB = prodPart(boxB, sigB, prodSize)
prodC = prodPart(boxC, sigC, prodSize)
prodD = prodPart(boxD, sigD, prodSize)

# Calculate the gap/interferece of the production
fit = prodA+prodB+prodC - prodD

# Printing standard deviation
print(fit)
print('Standard deviation of box fit:',stat.stdev(fit))

# Plotting all the assemblies (+ => gap / - => interference)
plt.figure()
plt.plot(fit)
plt.axhline(0, color = 'r')
plt.title('Plotting of all assemblies')

# plotting all the assemblies in a Histogram
plt.figure()
plt.hist(fit,bins='auto')
plt.axvline(0, color = 'r')
plt.title('Plotting of all assemblies as Histogram')


    