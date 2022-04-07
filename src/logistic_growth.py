from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# N = biomass
# t = time
# r = growth rate
# K = carrying capacity

# define model
def func(N,t,r,K):
    dydt = r*N*(1-(N/K))
    return dydt

# time points
t = linspace(0,80)

def plotODE(model, y0, t, r, K):
    y = odeint(model,y0,t,args=(r,K)) # solve diff eq
    plt.plot(t, y) # plot it

plotODE(func, 100, t, 0.05, 500)
plotODE(func, 100, t, 0.1, 500)

# plot results
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()