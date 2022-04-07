from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# N = biomass
# t = time
# r = growth rate
# K = carrying capacity

def model(N,t,r,K):
    dydt = r*N*(1-(N/K))
    return dydt

# time points
t = linspace(0,80)

# ODE 1
y0 = 50
r = 0.05
K = 500
y1 = odeint(model,y0,t,args=(r,K))

# ODE 2
y0 = 100
r = 0.1
K = 500
y2 = odeint(model,y0,t,args=(r,K))

# plot results
plt.plot(t,y1,linewidth=2)
plt.plot(t,y2,linewidth=2)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()