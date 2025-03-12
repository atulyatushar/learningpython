# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:35:54 2025

@author: atuly
"""
# Going from 0.0 to 10.0 in steps of 0.1
# using a for loop

from math import ceil
from numpy import zeros


n = int(ceil((10.0-0.0)/0.1)+1) 
x = zeros((n,1), float) #Create a 1D array

for i in range(n):
    x[i] = i*0.1

    