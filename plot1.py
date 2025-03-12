# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 23:27:14 2025

@author: atuly
"""
from numpy import array
import matplotlib.pyplot as plt

m = array([1.0, 2.0, 4.0, 6.0, 9.0, 11.0])
V = array([0.13, 0.26, 0.50, 0.77, 1.15, 1.36])

plt.plot(m, V, 'o')
plt.xlabel('m (kg)')
plt.ylabel('V (l)')
plt.show()

# yo


