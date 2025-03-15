# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:35:54 2025

@author: atuly
"""
# Generate and plot the function sin(x)
# Going from 0.0 to 10.0 in steps of 0.1
# using a for loop

from math import ceil
from numpy import zeros
from pylab import *

x0 = 0.0
x1 = 10.0
dx = 0.1
n = int(ceil((x1-x0)/dx)+1)

x = zeros((n,1), float) #Create a 1D array
y = zeros((n,1), float)

for i in range(n):
    x[i] = x0 + i*dx
    y[i] = sin(x[i])
plot (x,y)
show()
# End of program
# The output is the same as whileloop.py
# The for loop is more compact than the while loop


    