from math import ceil
from numpy import zeros
from pylab import *

x0 = 0.0
x1 = 10.0
dx = 0.1
n = int(ceil((x1-x0)/dx)+1)

x = zeros((n,1), float) #Create a 1D array
y = zeros((n,1), float)
i = 0
while i < n:
    x[i] = x0 + i*dx
    y[i] = sin(x[i])
    i += 1 # This is equivalent to i = i + 1
plot (x,y)
show()
# End of program
# The output is the same as forloop.py
# The while loop is more flexible than the for loop