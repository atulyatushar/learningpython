# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 23:46:50 2025

@author: atuly
"""

import numpy as np
import matplotlib.pyplot as plt

m = np.array([1.0, 2.0, 4.0, 6.0, 9.0, 11.0])
V = np.array([0.13, 0.26, 0.50, 0.77, 1.15, 1.36])
plt.plot(m, V, 'o')
plt.xlabel('m (kg)')
plt.ylabel('V (l)')

# Fit a linear regression line
slope, intercept = np.polyfit(m, V, 1)
plt.plot(m, slope * m + intercept, '-r')

# Add a title and show the plot
plt.title('Mass vs. Volume')
plt.grid(True)
plt.show()

# Calculate and print the density (slope represents 1/density)
density = 1/slope
print(f"The density is approximately {density:.2f} kg/l")