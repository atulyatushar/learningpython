# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 20:14:38 2025

@author: atuly
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
plt.plot(x,y, ':')
plt.show()

