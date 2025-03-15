from pylab import *
t0 = 0.0
t1 = 10.0
dt = 0.01
n = int(ceil((t1 - t0)/dt) + 1)
t = zeros (( n, 1), float)
y = zeros (( n, 1), float)
t[0] = t0
y[0] = 100.0 - 4.9*t[0]**2
i = 0
while y[i] > 0.0:
    i += 1
    t[i] = t0 + i*dt
    y[i] = 100.0 - 4.9*t[i]**2
# stop1
plot(t[0:i], y[0:i])
xlabel('t [s]'); ylabel('y [m]')
show()
